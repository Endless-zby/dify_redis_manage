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


class RedisStringSetTool(Tool):
    def _invoke(self, tool_parameters: dict[str, Any]) -> Generator[ToolInvokeMessage, None, None]:
        """
        Set a key-value pair in Redis
        """
        # 获取参数
        key = tool_parameters.get("key")
        value = tool_parameters.get("value")
        expire = tool_parameters.get("expire")
        logger.info(f"设置Redis键值对开始：{key}")
        
        # 参数验证
        if not validate_required_parameter(key, "Key", logger):
            yield self.create_text_message("Error: Key is required.")
            return
            
        if not validate_required_parameter(value, "Value", logger):
            yield self.create_text_message("Error: Value is required.")
            return

        try:
            # 获取Redis连接
            redis_client = get_redis_connection(self.runtime.credentials)
            
            # 在Redis中设置键值对
            if expire is not None:
                result = redis_client.set(key, value, ex=int(expire))
            else:
                result = redis_client.set(key, value)
            
            # 关闭连接
            redis_client.close()
            
            # 返回结果
            yield self.create_variable_message("result", result)
            
        except Exception as e:
            yield self.create_text_message(f"Error setting key-value in Redis: {str(e)}")