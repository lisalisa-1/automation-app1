import pytest
from appium import webdriver
from appium.options.common import AppiumOptions  # 导入通用的AppiumOptions
import threading
import time

from appium.webdriver.common.appiumby import AppiumBy

@pytest.fixture(scope="session", autouse=True)
# 定义设备1的操作逻辑（模拟器1：emulator-5554）
def run_device_1():
    # 使用AppiumOptions配置设备1的参数
    options_1 = AppiumOptions()
    # 设置安卓平台核心参数
    options_1.set_capability("platformName", "Android")
    options_1.set_capability("platformVersion", "12")  # 设备1的安卓版本
    options_1.set_capability("deviceName", "emulator-5554")  # 设备1唯一标识
    options_1.set_capability("udid", "emulator-5554")

    options_1.set_capability("appPackage", "io.appium.android.apis")  # 要启动的APP包名
    options_1.set_capability("appActivity", "io.appium.android.apis.ApiDemos")  # APP入口Activity
    options_1.set_capability("automationName", "UiAutomator2")  # 安卓自动化引擎
    options_1.set_capability("noReset", True)  # 不重置APP状态
    options_1.set_capability("newCommandTimeout", 300)  # 命令超时时间

    # 连接同一个Appium Server，创建设备1的会话
    driver1 = webdriver.Remote("http://127.0.0.1:4723", options=options_1)
    yield driver1
    driver1.quit()


def case1(driver):
    # 设备1的操作示例：停留5秒模拟操作
    el1 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Access'ibility")
    el1.click()
    el2 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Accessibility Node Provider")
    el2.click()
    el3 = driver.find_element(by=AppiumBy.CLASS_NAME, value="android.view.View")
    el3.click()

    #driver.quit()
    print("设备1会话结束")
# 定义设备2的操作逻辑（模拟器2：emulator-5556）
@pytest.fixture(scope="session", autouse=True)
def run_device_2():
    # 使用AppiumOptions配置设备2的参数
    options_2 = AppiumOptions()
    # 设置安卓平台核心参数
    options_2.set_capability("platformName", "Android")
    options_2.set_capability("platformVersion", "13")  # 设备2的安卓版本
    options_2.set_capability("deviceName", "24ecd0a2")  # 设备2唯一标识
    options_2.set_capability("appPackage", "io.appium.android.apis")
    options_2.set_capability("appActivity", "io.appium.android.apis.ApiDemos")
    options_2.set_capability("udid", "24ecd0a2")

    options_2.set_capability("automationName", "UiAutomator2")
    options_2.set_capability("noReset", True)
    options_2.set_capability("newCommandTimeout", 300)

    # 连接同一个Appium Server，创建设备2的会话
    driver2 = webdriver.Remote("http://127.0.0.1:4723", options=options_2)
    yield driver2
    driver2.quit()


# 4. 测试用例（每个用例只执行一次，自动分配到空闲设备）
def test_open_settings(run_device_2):
    driver = run_device_2
    el1 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Animation")
    el1.click()
    el2 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Events")
    el2.click()
    driver.back()
    driver.back()


def test_click_wifi(run_device_1):
    driver = run_device_1
    el1 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Animation")
    el1.click()
    el2 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Events")
    el2.click()
    driver.back()
    driver.back()


def test_check_battery(run_device_2):
    driver = run_device_2
    el1 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Animation")
    el1.click()
    el2 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Events")
    el2.click()
    driver.back()
    driver.back()

#
#
# # 多线程并行执行两台设备的操作
# if __name__ == "__main__":
#     # 注意：需提前启动Appium Server（终端执行：appium --port 4723）
#     # 创建线程
#     thread1 = threading.Thread(target=run_device_1)
#     thread2 = threading.Thread(target=run_device_2)
#
#     # 启动线程
#     thread1.start()
#     thread2.start()
#
#     # 等待线程执行完成
#     # thread1.join()
#     # thread2.join()
#
#     print("设备1和设备2操作并行执行")
#
#     print("两台设备操作均已完成")