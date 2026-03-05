import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#from appium.webdriver.common.action_chains import ActionChains
#from appium.webdriver.common.touch_action import TouchAction
import time

import allure

@pytest.fixture(scope="module")
def driver():
    """创建并管理Appium驱动实例"""
    options = UiAutomator2Options()
    options.udid="emulator-5554"
    options.platform_name = 'Android'
    options.device_name = '111'
    #options.app = 'path/to/ApiDemos-debug.apk'
    options.app_package = 'io.appium.android.apis'
    options.app_activity = '.ApiDemos'

    # 修复Appium Server URL，添加/wd/hub后缀
    driver_instance = webdriver.Remote('http://localhost:4723', options=options)
    driver_instance.implicitly_wait(10)
    # 测试前准备
    print("测试开始，已连接到设备")
    
    # 提供驱动实例给测试用例
    yield driver_instance
    
    # 测试后清理
    #driver_instance.quit()
    print("测试结束，正在关闭驱动")

@allure.feature("UI交互测试")  # 大模块
@allure.story("Spinner下拉选择")  # 子功能
@allure.severity(allure.severity_level.CRITICAL)  # 优先级
def test_accessibility_node_provider(driver):
    """测试Accessibility Node Provider功能"""
    # 执行操作
    print("点击Access'ibility按钮")
    el1 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Access'ibility")
    el1.click()
    
    print("点击Accessibility Node Provider按钮")
    el2 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Accessibility Node Provider")
    el2.click()
    
    print("测试完成")
    # 返回上一页
    driver.back()




@allure.feature("UI交互测试")
@allure.story("Checkbox状态验证")
@allure.severity(allure.severity_level.NORMAL)
def test_button_operations(driver):
    """测试按钮控件操作"""
    print("\n测试按钮控件操作")
    
    # 点击Views
    driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Views").click()
    
    # 点击Buttons
    driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Buttons").click()
    
    # 点击不同类型的按钮
    buttons = [
        "Normal",
        "Small",
        "Toggle",
        "Disabled Button"
    ]
    
    for button_name in buttons:
        try:
            button = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value=button_name)
            if button_name != "Disabled Button":  # 禁用按钮无法点击
                button.click()
                print(f"已点击: {button_name}")
                time.sleep(0.5)
        except Exception as e:
            print(f"点击{button_name}时出错: {e}")
    
    # 返回上一页
    driver.back()
    driver.back()

def test_text_fields(driver):
    """测试文本输入框操作"""
    print("\n测试文本输入框操作")
    
    # 点击Views
    driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Views").click()
    
    # 添加向下滑动操作，因为TextFields控件可能不在当前可见区域
    print("正在向下滑动以查找TextFields控件")
    # 获取屏幕尺寸
    screen_size = driver.get_window_size()
    screen_width = screen_size['width']
    screen_height = screen_size['height']
    
    # 计算滑动的起始和结束位置
    start_x = screen_width // 2
    start_y = screen_height * 3 // 4  # 屏幕下方
    end_x = screen_width // 2
    end_y = screen_height // 4  # 屏幕上方
    
    # 执行向下滑动
    driver.swipe(start_x, start_y, end_x, end_y, duration=1000)
    time.sleep(1)  # 等待滑动完成
    
    # 点击TextFields
    driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="TextFields").click()
    
    # 修复find_element方法参数错误
    text_field = driver.find_element(by=AppiumBy.CLASS_NAME, value="android.widget.EditText")
    
    # 清除文本（如果有）
    text_field.clear()
    
    # 输入文本
    test_text = "Hello Appium!"
    text_field.send_keys(test_text)
    print(f"已在文本框中输入: {test_text}")
    
    # 获取输入的文本并验证
    entered_text = text_field.text
    # 这里加上pytest断言，验证entered_text==test_text
    assert entered_text == test_text, f"预期文本: {test_text}, 实际文本: {entered_text}"

    print(f"获取到的文本: {entered_text}")
    
    # 返回上一页
    driver.back()
    driver.back()

    with pytest.raises(NoSuchElementException, match="no such element"):
        # 故意定位不存在的元素
        driver.find_element("id", "不存在的元素ID")

        # 进阶：捕获异常并验证详情
    with pytest.raises(NoSuchElementException) as exc_info:
        driver.find_element("id", "不存在的元素ID")
    assert "Unable to locate element" in str(exc_info.value), "异常信息不符合预期"

def test_checkboxes(driver):
    """测试复选框操作"""
    print("\n测试复选框操作")
    
    # 点击Views
    driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Views").click()
    
    # 添加向下滑动操作，因为Controls控件可能不在当前可见区域
    print("正在向下滑动以查找Controls控件")
    screen_size = driver.get_window_size()
    # driver.swipe(screen_size['width']//2, screen_size['height']*3//4,
    #              screen_size['width']//2, screen_size['height']//4, duration=1000)
    # time.sleep(1)
    
    # 点击Controls
    driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Controls").click()
    
    # 点击2. Light Theme
    driver.find_element(by=AppiumBy.XPATH, value="//android.widget.TextView[@text='1. Light Theme']").click()
    
    # 找到所有复选框
    checkboxes = driver.find_elements(by=AppiumBy.CLASS_NAME, value="android.widget.CheckBox")
    
    for i, checkbox in enumerate(checkboxes):
        # 获取复选框状态
        #is_checked = checkbox.get_attribute("checked") == "true"
        #print(checkbox.get_attribute("checked"))
        print(f"复选框{i+1}初始状态: {'已选中' if checkbox.is_selected() else '未选中'}")
        print(checkbox.is_selected())
        if not checkbox.is_selected():
            checkbox.click()
            #time.sleep(5)
            print(checkbox.is_selected())
            print("checked:"+checkbox.get_attribute("checked"))

            print("selectd:"+checkbox.get_attribute("selected"))
            # 点击切换状态


        print(f"复选框{i+1}初始状态: {'已选中' if checkbox.is_selected()  else '未选中'}")

    radiobuttons = driver.find_elements(by=AppiumBy.CLASS_NAME, value="android.widget.RadioButton")
    for i, radio_button in enumerate(radiobuttons):
        radio_button.click()
        radio_button.click()


    # 返回上一页
    driver.back()
    driver.back()
    driver.back()

def test_radio_buttons(driver):
    """测试单选按钮操作"""
    print("\n测试单选按钮操作")
    
    # 点击Views
    driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Views").click()
    
    # 添加向下滑动操作，因为Controls控件可能不在当前可见区域
    print("正在向下滑动以查找Controls控件")

    
    # 点击Controls
    driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Controls").click()
    
    # 点击2. Light Theme
    driver.find_element(by=AppiumBy.XPATH, value="//android.widget.TextView[@text='1. Light Theme']").click()
    
    # 找到所有单选按钮
    radio_buttons = driver.find_elements(by=AppiumBy.CLASS_NAME, value="android.widget.RadioButton")
    
    for i, radio_button in enumerate(radio_buttons):
        # 点击单选按钮
        radio_button.click()
        print(f"已选择单选按钮: {i+1}")
        
        # 验证是否被选中
        is_selected = radio_button.get_attribute("checked") == "true"
        print(f"单选按钮{i+1}状态: {'已选中' if is_selected else '未选中'}")
        time.sleep(0.5)
    
    # 返回上一页
    driver.back()
    driver.back()
    driver.back()



def test_list_view(driver):
    """测试列表视图操作"""
    print("\n测试列表视图操作")
    
    # 点击Views
    driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Views").click()
    
    # 添加向下滑动操作，因为List控件可能不在当前可见区域
    print("正在向下滑动以查找List控件")
    screen_size = driver.get_window_size()
    # 可能需要多次滑动才能找到List

    
    # 点击List
    driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Lists").click()
    
    # 点击Single Choice
    driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="10. Single choice list").click()
    
    # 找到列表项
    list_items = driver.find_elements(by=AppiumBy.CLASS_NAME, value="android.widget.CheckedTextView")
    
    # 打印前5个列表项
    print("列表项内容:")
    for i, item in enumerate(list_items[:5]):
        print(f"  {i+1}. {item.text}")
    
    # 选择第三个列表项
    list_items[2].click()
    print("已选择第三个列表项")
    time.sleep(0.5)
    
    # 返回上一页
    driver.back()
    driver.back()
    driver.back()

def test_switch_control(driver):
    """测试开关控件操作"""
    print("\n测试开关控件操作")
    
    # 点击Views
    driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Views").click()
    
    # 添加向下滑动操作，因为Controls控件可能不在当前可见区域

    # 点击Controls
    driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Controls").click()
    
    # 点击2. Light Theme
    driver.find_element(by=AppiumBy.XPATH, value="//android.widget.TextView[@text='1. Light Theme']").click()
    
    # 找到开关控件
    switch_control = driver.find_element(by=AppiumBy.ID, value="io.appium.android.apis:id/toggle1")

    el1 = driver.find_element(by=AppiumBy.ID, value="io.appium.android.apis:id/edit")
    el1.send_keys("2323")
    el2 = driver.find_element(by=AppiumBy.ID, value="io.appium.android.apis:id/toggle1")
    el2.click()
    el3 = driver.find_element(by=AppiumBy.ID, value="io.appium.android.apis:id/spinner1")
    el3.click()

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((AppiumBy.XPATH, "//android.widget.CheckedTextView"))
    )
    options = driver.find_elements(AppiumBy.CLASS_NAME, "android.widget.CheckedTextView")
    options[2].click()
    
    # 返回上一页
    driver.back()
    driver.back()
    driver.back()

def test_wait(driver):
    driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Views").click()

    screen_size = driver.get_window_size()
    screen_width = screen_size['width']
    screen_height = screen_size['height']

    # 计算滑动的起始和结束位置
    start_x = screen_width // 2
    start_y = screen_height * 3 // 4  # 屏幕下方
    end_x = screen_width // 2
    end_y = screen_height // 4  # 屏幕上方

    # 执行向下滑动
    driver.swipe(start_x, start_y, end_x, end_y, duration=1000)



    # WebDriverWait(driver, 10).until(
    #     EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, "")))

    driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Buttons").click()



if __name__ == "__main__":
    # 可以直接运行此脚本进行测试
    pytest.main(["-v", "test_u1.py"])