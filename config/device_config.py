# 设备配置
import os


class DeviceConfig:
    """设备配置"""
    
    # 设备信息
    DEVICE_UDID = os.environ.get('DEVICE_UDID', '24ecd0a2')
    DEVICE_NAME = os.environ.get('DEVICE_NAME', '24ecd0a2')
    PLATFORM_NAME = os.environ.get('PLATFORM_NAME', 'Android')
    
    # Appium服务
    APPIUM_HOST = os.environ.get('APPIUM_HOST', 'localhost')
    APPIUM_PORT = int(os.environ.get('APPIUM_PORT', '4726'))
    
    # 驱动版本
    DRIVER_VERSION = os.environ.get('DRIVER_VERSION', 'latest')