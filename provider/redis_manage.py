from typing import Any
import redis as db

from urllib.parse import urlparse

from dify_plugin import ToolProvider
from dify_plugin.errors.tool import ToolProviderCredentialValidationError

# 导入 logging 和自定义处理器
import logging
from dify_plugin.config.logger_format import plugin_logger_handler

# 使用自定义处理器设置日志
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
logger.addHandler(plugin_logger_handler)


class RedisManageProvider(ToolProvider):

    def _validate_credentials(self, credentials: dict[str, Any]) -> None:
        try:
            """
            IMPLEMENT YOUR VALIDATION HERE
            """
            redis_host = credentials.get("REDIS_HOST")
            redis_port = credentials.get("REDIS_PORT")
            redis_password = credentials.get("REDIS_PASSWORD", None)

        except Exception as e:
            raise ToolProviderCredentialValidationError(str(e))
        # 尝试连接Redis
        try:
            # 创建Redis连接
            r = db.Redis(
                host=redis_host,
                port=redis_port,
                password=redis_password,
                socket_connect_timeout=5  # 5秒超时
            )
            # 测试连接
            r.ping()
            logger.info("Redis连接正常")

        except Exception as e:
            logger.error(f"Redis连接失败: {str(e)}")
            raise ToolProviderCredentialValidationError(str(e))
        r.close()
        logger.info("验证完成,关闭连接")
