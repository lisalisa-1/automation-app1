import os
from typing import Dict, Any
import yaml
from dotenv import load_dotenv
from pydantic_settings import BaseSettings
from pydantic import ConfigDict
# 加载环境变量（优先指定环境）
def load_env(env: str = "test"):
    env_file = f".env.{env}"
    current_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(current_dir)
    env_file = os.path.join(project_root, env_file)
    if os.path.exists(env_file):
        load_dotenv(env_file, override=True)
    else:
        raise FileNotFoundError(f"环境配置文件 {env_file} 不存在")

# 加载 YAML 配置
def load_yaml(file_path: str) -> Dict[str, Any]:


    if not os.path.exists(file_path):
        raise FileNotFoundError(f"YAML 文件 {file_path} 不存在")
    with open(file_path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)

# Appium 3.X 服务配置模型
class Appium3Settings(BaseSettings):
    driver_name: str = "uiautomator2"
    driver_version: str = "3.0.0"
    server_host: str = "127.0.0.1"
    server_port: int = 4726
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

# 全局配置初始化
load_env("test")  # 默认加载测试环境
appium3_cfg = Appium3Settings()
app_cfg = AppSettings()
device_cfg = DeviceSettings()

current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(current_dir)
yaml_file = os.path.join(project_root, 'appium_config/driver.yaml')

appium3_yaml = load_yaml(yaml_file)
print(1)

