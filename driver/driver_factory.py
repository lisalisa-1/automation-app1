# 单例模式管理Driver，确保全局只有一个Driver实例
from appium import webdriver
from appium.options.android import UiAutomator2Options
from config.config import Config

# 全局Driver实例
_driver = None

def get_driver():
    """获取Driver实例（单例）"""
    global _driver
    if _driver is None:
        options = UiAutomator2Options()
        options.platform_name = Config.PLATFORM_NAME
        options.udid = Config.UDID
        options.device_name = Config.DEVICE_NAME
        options.app_package = Config.APP_PACKAGE
        options.app_activity = Config.APP_ACTIVITY
        # 提升稳定性的可选配置
        options.no_reset = True  # 不重置App状态
        options.auto_grant_permissions = True  # 自动授予权限
        options.new_command_timeout = 30  # 新命令超时

        _driver = webdriver.Remote(Config.APPIUM_URL, options=options)
        _driver.implicitly_wait(Config.IMPLICITLY_WAIT)
        print("✅ Driver创建成功")
    return _driver

def quit_driver():
    """销毁Driver"""
    global _driver
    if _driver:
        _driver.quit()
        _driver = None
        print("❌ Driver已销毁")