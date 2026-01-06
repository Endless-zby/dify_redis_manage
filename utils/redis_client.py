import redis
import logging
from typing import Any, Optional


def get_redis_connection(credentials: dict[str, Any]) -> redis.Redis:
    """
    根据凭证信息创建Redis连接
    
    Args:
        credentials: 包含Redis连接信息的字典
        
    Returns:
        redis.Redis: Redis连接对象
    """
    redis_host = credentials.get("REDIS_HOST", "localhost")
    redis_port = int(credentials.get("REDIS_PORT", 6379))
    redis_db = int(credentials.get("REDIS_DB", 0))
    redis_password = credentials.get("REDIS_PASSWORD")
    
    # 创建Redis连接
    redis_client = redis.Redis(
        host=redis_host,
        port=redis_port,
        db=redis_db,
        password=redis_password if redis_password else None,
        decode_responses=True
    )
    
    return redis_client


def validate_required_parameter(param: Any, param_name: str, logger: logging.Logger) -> bool:
    """
    验证必需参数是否存在
    
    Args:
        param: 要验证的参数值
        param_name: 参数名称
        logger: 日志记录器
        
    Returns:
        bool: 参数是否有效
    """
    if not param:
        logger.info(f"Error: {param_name} is required.")
        return False
    return True