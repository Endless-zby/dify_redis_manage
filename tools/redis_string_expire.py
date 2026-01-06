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


class RedisStringExpireTool(Tool):
    def _invoke(self, tool_parameters: dict[str, Any]) -> Generator[ToolInvokeMessage, None, None]:
        """
        Set a timeout on a key
        """
        # 获取参数
        key = tool_parameters.get("key")
        seconds = tool_parameters.get("seconds")
        logger.info(f"设置Redis键过期时间开始：{key}")
        
        # 参数验证
        if not validate_required_parameter(key, "Key", logger):
            yield self.create_text_message("Error: Key is required.")
            return
            
        if not validate_required_parameter(seconds, "Seconds", logger):
            yield self.create_text_message("Error: Seconds is required.")
            return

        try:
            # 获取Redis连接
            redis_client = get_redis_connection(self.runtime.credentials)
            
            # 设置键的过期时间
            result = redis_client.expire(key, int(seconds))
            
            # 关闭连接
            redis_client.close()
            
            # 返回结果
            yield self.create_variable_message("result", result)
            
        except Exception as e:
            yield self.create_text_message(f"Error setting expire time in Redis: {str(e)}")