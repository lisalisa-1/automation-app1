import time
from loguru import logger

import pytest
import queue
from appium import webdriver
from appium.options.common import AppiumOptions
from threading import Lock

from appium.webdriver.common.appiumby import AppiumBy

# 1. 全局设备池（存放空闲设备的Driver）
DEVICE_QUEUE = queue.Queue()
QUEUE_LOCK = Lock()


# 2. 初始化设备池（所有设备只启动一次）
@pytest.fixture(scope="session", autouse=True)
def init_device_pool():
    # 设备配置列表
    DEVICE_CONFIGS = [{
        "platformName": "Android",  # 平台类型（固定为Android）    # 设备1：模拟器 emulator-5554
        "platformVersion": "13",  # 设备安卓版本（根据实际修改）
        "deviceName": "emulator-5554",  # 设备唯一标识（adb devices输出的名称）
        "udid": "emulator-5554",  # 设备UDID（模拟器与deviceName一致，真机填实际UDID）
        "appPackage": "io.appium.android.apis",  # 要测试的APP包名（示例：设置APP）
        "appActivity": "io.appium.android.apis.ApiDemos",  # APP启动入口Activity
        "automationName": "UiAutomator2",  # 安卓自动化引擎（固定为UiAutomator2）
        # ========== 新增/关键配置 ==========
        "systemPort": 8205,  # 多设备必须唯一（8200-8299），避免端口冲突
        "noReset": True,  # 不重置APP，避免重复安装
        "fullReset": False,
        "ignoreHiddenApiPolicyError": True,  # 安卓10+必需，解决API限制
        "skipServerInstallation": False,  # 强制重新安装UiAutomator2 Server
        "newCommandTimeout": 300,  # 延长超时，避免会话断开
        "disableWindowAnimation": True,  # 关闭动画，提升稳定性
        "autoGrantPermissions": True,  # 自动授权，避免弹窗阻塞
    },
        # 设备2：模拟器 emulator-5556
        {
            "platformName": "Android",
            "platformVersion": "13",  # 设备2的安卓版本（可与设备1不同）
            "deviceName": "24ecd0a2",
            "udid": "24ecd0a2",
            "appPackage": "io.appium.android.apis",
            "appActivity": "io.appium.android.apis.ApiDemos",
            "automationName": "UiAutomator2",
            # ========== 新增/关键配置 ==========
            "systemPort": 8206,  # 多设备必须唯一（8200-8299），避免端口冲突
            "noReset": True,  # 不重置APP，避免重复安装
            "fullReset": False,
            "ignoreHiddenApiPolicyError": True,  # 安卓10+必需，解决API限制
            "skipServerInstallation": False,  # 强制重新安装UiAutomator2 Server
            "newCommandTimeout": 300,  # 延长超时，避免会话断开
            "disableWindowAnimation": True,  # 关闭动画，提升稳定性
            "autoGrantPermissions": True,  # 自动授权，避免弹窗阻塞

        }
    ]

    # 启动所有设备，放入队列
    for caps in DEVICE_CONFIGS:
        options = AppiumOptions()
        options.load_capabilities(caps)
        driver = webdriver.Remote("http://127.0.0.1:4723", options=options)
        DEVICE_QUEUE.put(driver)
        logger.info(f"📱 设备{caps['deviceName']}已加入空闲池")

    yield  # 所有用例执行完后，关闭所有设备
    while not DEVICE_QUEUE.empty():
        driver = DEVICE_QUEUE.get()
        driver.quit()
        logger.info(f"📱 设备{driver.capabilities['deviceName']}已关闭")


# 3. Fixture：获取空闲设备（每个用例只拿一台）
@pytest.fixture(scope="function")
def appium_driver():
    # 从队列获取空闲设备（阻塞等待，直到有空闲）
    with QUEUE_LOCK:
        driver = DEVICE_QUEUE.get()
    logger.info(f"\n===== 占用设备：{driver.capabilities['deviceName']} =====")

    yield driver

    # 用例执行完，归还设备到队列
    with QUEUE_LOCK:
        DEVICE_QUEUE.put(driver)
    logger.info(f"===== 释放设备：{driver.capabilities['deviceName']} =====")

@pytest.fixture(scope="function")
def appium_driver():
    # 从队列获取空闲设备（阻塞等待，直到有空闲）
    with QUEUE_LOCK:
        driver = DEVICE_QUEUE.get()
    logger.info(f"\n===== 占用设备：{driver.capabilities['deviceName']} =====")

    yield driver

    # 用例执行完，归还设备到队列
    with QUEUE_LOCK:
        DEVICE_QUEUE.put(driver)
    logger.info(f"===== 释放设备：{driver.capabilities['deviceName']} =====")


# 4. 测试用例（每个用例只执行一次，自动分配到空闲设备）
def test_open_settings(appium_driver):
    driver = appium_driver

    el1 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Animation")
    el1.click()
    time.sleep(5)


def test_click_wifi(appium_driver):
    driver = appium_driver

    el1 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Animation")
    el1.click()
    time.sleep(5)


def test_check_battery(appium_driver):
    driver = appium_driver
    el1 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Animation")
    el1.click()
    el2 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Events")
    el2.click()
    time.sleep(7)


