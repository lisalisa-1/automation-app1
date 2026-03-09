# 无需任何线程代码，仅需参数化+Fixture
import time

import pytest
from appium.options.common import AppiumOptions
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

# 完整的多设备配置列表（适配安卓模拟器/真机，可直接复制使用）
DEVICE_CONFIGS =  [{
        "platformName": "Android",          # 平台类型（固定为Android）    # 设备1：模拟器 emulator-5554

        "platformVersion": "13",            # 设备安卓版本（根据实际修改）
        "deviceName": "emulator-5554",      # 设备唯一标识（adb devices输出的名称）
        "udid": "emulator-5554",            # 设备UDID（模拟器与deviceName一致，真机填实际UDID）
        "appPackage": "io.appium.android.apis",  # 要测试的APP包名（示例：设置APP）
        "appActivity": "io.appium.android.apis.ApiDemos",         # APP启动入口Activity
        "automationName": "UiAutomator2",   # 安卓自动化引擎（固定为UiAutomator2）
    }   ,
    # 设备2：模拟器 emulator-5556
    {
        "platformName": "Android",
        "platformVersion": "13",            # 设备2的安卓版本（可与设备1不同）
        "deviceName": "24ecd0a2",
        "udid": "24ecd0a2",
        "appPackage": "io.appium.android.apis",
        "appActivity": "io.appium.android.apis.ApiDemos",
        "automationName": "UiAutomator2",

    }
]


@pytest.fixture(scope="function", params=DEVICE_CONFIGS)
def appium_driver(request):
    # 通用Driver创建逻辑（适配所有设备）
    caps = request.param
    options = AppiumOptions()
    options.load_capabilities(caps)
    driver = webdriver.Remote("http://127.0.0.1:4723", options=options)
    case1(driver)
    yield driver
    driver.quit()

def case1(driver):
    # 设备1的操作示例：停留5秒模拟操作
    el1 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Access'ibility")
    el1.click()
    time.sleep(5)
    el2 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Accessibility Node Provider")
    el2.click()
    el3 = driver.find_element(by=AppiumBy.CLASS_NAME, value="android.view.View")
    el3.click()
def test_open_settings(appium_driver):
    # 通用用例逻辑（自动适配所有设备）
     assert appium_driver.current_package == "io.appium.android.apis"
