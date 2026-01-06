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


class RedisGeoPosTool(Tool):
    def _invoke(self, tool_parameters: dict[str, Any]) -> Generator[ToolInvokeMessage, None, None]:
        """
        Get the position of geospatial items
        """
        # 获取参数
        key = tool_parameters.get("key")
        members_str = tool_parameters.get("members")
        logger.info(f"从Redis获取地理位置信息：{key}")
        
        # 参数验证
        if not validate_required_parameter(key, "Key", logger):
            yield self.create_text_message("Error: Key is required.")
            return
            
        if not validate_required_parameter(members_str, "Members", logger):
            yield self.create_text_message("Error: Members is required.")
            return
            
        # 将逗号分隔的字符串转换为列表
        members = [member.strip() for member in members_str.split(',')]

        try:
            # 获取Redis连接
            redis_client = get_redis_connection(self.runtime.credentials)
            
            # 获取地理位置信息
            positions = redis_client.geopos(key, *members)
            
            # 关闭连接
            redis_client.close()
            
            # 格式化结果
            result = []
            for pos in positions:
                if pos is None:
                    result.append(None)
                else:
                    result.append({
                        "longitude": pos[0],
                        "latitude": pos[1]
                    })
            
            # 返回结果
            yield self.create_variable_message("positions", result)
            
        except Exception as e:
            yield self.create_text_message(f"Error getting geospatial positions from Redis: {str(e)}")