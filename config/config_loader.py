import os
from dotenv import load_dotenv
from pydantic_settings import BaseSettings
from pydantic import ConfigDict
from loguru import logger
# 加载环境变量（优先指定环境）
def load_env(env: str = "test"):
    env_file = f".env.{env}"
    current_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(current_dir)
    env_file = os.path.join(project_root, env_file)
    if os.path.exists(env_file):
        load_dotenv(env_file, override=True)
        logger.info(f"成功加载环境配置文件：{env_file}")
    else:
        raise FileNotFoundError(f"环境配置文件 {env_file} 不存在")


# Appium 3.X 服务配置模型
class Appium3Settings(BaseSettings):
    driver_name: str = "uiautomator2"
    driver_version: str = "3.0.0"
    server_host: str = "127.0.0.1"
    server_port: int = 4723
    log_level: str = "info"

    model_config = ConfigDict(
        env_prefix="APPIUM_",  # 环境变量前缀：APPIUM_DRIVER_NAME
        case_sensitive=False
    )

# App 配置模型
class AppSettings(BaseSettings):
    package: str
    activity: str
    app_path: str
    base_url: str  # 接口基础地址

    model_config = ConfigDict(
        env_prefix="APP_",
        case_sensitive=False
    )

# 设备配置模型
class DeviceSettings(BaseSettings):
    platform_name: str = "Android"
    platform_version: str
    device_name: str
    udid: str

    model_config = ConfigDict(
        env_prefix="DEVICE_",
        case_sensitive=False
    )


