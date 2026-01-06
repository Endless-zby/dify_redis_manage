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


class RedisGeoRadiusTool(Tool):
    def _invoke(self, tool_parameters: dict[str, Any]) -> Generator[ToolInvokeMessage, None, None]:
        """
        Get geospatial items within a radius from a point
        """
        # 获取参数
        key = tool_parameters.get("key")
        longitude = tool_parameters.get("longitude")
        latitude = tool_parameters.get("latitude")
        radius = tool_parameters.get("radius")
        unit = tool_parameters.get("unit")
        logger.info(f"在Redis中搜索指定半径范围内的地理位置项：{key}")
        
        # 参数验证
        if not validate_required_parameter(key, "Key", logger):
            yield self.create_text_message("Error: Key is required.")
            return
            
        if not validate_required_parameter(longitude, "Longitude", logger):
            yield self.create_text_message("Error: Longitude is required.")
            return
            
        if not validate_required_parameter(latitude, "Latitude", logger):
            yield self.create_text_message("Error: Latitude is required.")
            return
            
        if not validate_required_parameter(radius, "Radius", logger):
            yield self.create_text_message("Error: Radius is required.")
            return
            
        if not validate_required_parameter(unit, "Unit", logger):
            yield self.create_text_message("Error: Unit is required.")
            return

        try:
            # 获取Redis连接
            redis_client = get_redis_connection(self.runtime.credentials)
            
            # 获取指定半径范围内的地理位置项
            members = redis_client.georadius(key, longitude, latitude, radius, unit=unit)
            
            # 关闭连接
            redis_client.close()
            
            # 返回结果
            yield self.create_variable_message("members", members)
            
        except Exception as e:
            yield self.create_text_message(f"Error searching geospatial items in Redis: {str(e)}")