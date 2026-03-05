import os
from loguru import logger
from datetime import datetime

def init_logger():
    """初始化日志配置"""
    # 创建日志目录
    log_dir = "logs"
    os.makedirs(log_dir, exist_ok=True)
    print(f"当前工作目录：{os.getcwd()}")

    print(f"file目录：{__file__}")
    # 日志文件
    log_file = os.path.join(log_dir, f"appium3_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log")
    # 配置 loguru
    logger.add(
        log_file,
        rotation="500 MB",  # 日志轮转
        retention="7 days",  # 保留 7 天
        compression="zip",   # 压缩旧日志
        level="INFO",
        format="{time:YYYY-MM-DD HH:mm:ss} | {level} | {module}:{line} | {message}"
    )
    logger.info("✅ 日志系统初始化完成，在log_utils文件中")
