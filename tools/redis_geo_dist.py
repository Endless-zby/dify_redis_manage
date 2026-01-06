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


class RedisGeoDistTool(Tool):
    def _invoke(self, tool_parameters: dict[str, Any]) -> Generator[ToolInvokeMessage, None, None]:
        """
        Get the distance between two geospatial items
        """
        # 获取参数
        key = tool_parameters.get("key")
        member1 = tool_parameters.get("member1")
        member2 = tool_parameters.get("member2")
        unit = tool_parameters.get("unit", "m")
        logger.info(f"计算Redis中两个地理位置项的距离：{key}")
        
        # 参数验证
        if not validate_required_parameter(key, "Key", logger):
            yield self.create_text_message("Error: Key is required.")
            return
            
        if not validate_required_parameter(member1, "Member1", logger):
            yield self.create_text_message("Error: Member1 is required.")
            return
            
        if not validate_required_parameter(member2, "Member2", logger):
            yield self.create_text_message("Error: Member2 is required.")
            return

        try:
            # 获取Redis连接
            redis_client = get_redis_connection(self.runtime.credentials)
            
            # 计算两个地理位置项之间的距离
            distance = redis_client.geodist(key, member1, member2, unit=unit)
            
            # 关闭连接
            redis_client.close()
            
            # 返回结果
            yield self.create_variable_message("distance", distance)
            
        except Exception as e:
            yield self.create_text_message(f"Error calculating geospatial distance in Redis: {str(e)}")