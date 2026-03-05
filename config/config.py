# 集中管理所有配置，避免硬编码
class Config:
    # Appium服务配置
    APPIUM_SERVER = "http://localhost:4726"
    APPIUM_PATH = "/wd/hub"
    #APPIUM_URL = f"{APPIUM_SERVER}{APPIUM_PATH}"
    APPIUM_URL = f"{APPIUM_SERVER}"

    # 设备配置
    PLATFORM_NAME = "Android"
    UDID = "24ecd0a2"  # 替换为你的设备UDID
    DEVICE_NAME = "Android Device"

    # App配置
    APP_PACKAGE = "com.xiaomi.shop"
    APP_ACTIVITY = "com.xiaomi.shop2.activity.MainActivity"

    # 超时配置
    IMPLICITLY_WAIT = 10  # 隐式等待
    EXPLICITLY_WAIT = 10  # 显式等待

    # 报告配置
    ALLURE_RESULTS = "./reports/allure-results"
    ALLURE_HTML = "./reports/allure-report"
    SCREENSHOT_DIR = "./reports/screenshots/"