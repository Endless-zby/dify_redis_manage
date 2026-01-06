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


class RedisListRpushTool(Tool):
    def _invoke(self, tool_parameters: dict[str, Any]) -> Generator[ToolInvokeMessage, None, None]:
        """
        Insert all the specified values at the tail of the list stored at key
        """
        # 获取参数
        key = tool_parameters.get("key")
        values_str = tool_parameters.get("values")
        logger.info(f"向Redis列表尾部插入值：{key}")
        
        # 参数验证
        if not validate_required_parameter(key, "Key", logger):
            yield self.create_text_message("Error: Key is required.")
            return
            
        if not validate_required_parameter(values_str, "Values", logger):
            yield self.create_text_message("Error: Values is required.")
            return
            
        # 将逗号分隔的字符串转换为列表
        values = [value.strip() for value in values_str.split(',')]

        try:
            # 获取Redis连接
            redis_client = get_redis_connection(self.runtime.credentials)
            
            # 向列表尾部插入值
            length = redis_client.rpush(key, *values)
            
            # 关闭连接
            redis_client.close()
            
            # 返回结果
            yield self.create_variable_message("length", length)
            
        except Exception as e:
            yield self.create_text_message(f"Error pushing values to list in Redis: {str(e)}")