from collections.abc import Generator
from typing import Any

from dify_plugin import Tool
from dify_plugin.entities.tool import ToolInvokeMessage

# 导入 logging 和自定义处理器
import logging
from dify_plugin.config.logger_format import plugin_logger_handler

# 导入公共工具
from utils.redis_client import get_redis_connection, validate_required_parameter

# 使用自定义处理器设置日志
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
logger.addHandler(plugin_logger_handler)


class RedisListLtrimTool(Tool):
    def _invoke(self, tool_parameters: dict[str, Any]) -> Generator[ToolInvokeMessage, None, None]:
        """
        Trim an existing list so that it will contain only the specified range of elements
        """
        # 获取参数
        key = tool_parameters.get("key")
        start = tool_parameters.get("start")
        stop = tool_parameters.get("stop")
        logger.info(f"修剪Redis列表：{key}")
        
        # 参数验证
        if not validate_required_parameter(key, "Key", logger):
            yield self.create_text_message("Error: Key is required.")
            return
            
        if not validate_required_parameter(start, "Start", logger):
            yield self.create_text_message("Error: Start is required.")
            return
            
        if not validate_required_parameter(stop, "Stop", logger):
            yield self.create_text_message("Error: Stop is required.")
            return

        try:
            # 获取Redis连接
            redis_client = get_redis_connection(self.runtime.credentials)
            
            # 修剪列表
            result = redis_client.ltrim(key, start, stop)
            
            # 关闭连接
            redis_client.close()
            
            # 返回结果
            yield self.create_variable_message("result", result)
            
        except Exception as e:
            yield self.create_text_message(f"Error trimming list in Redis: {str(e)}")