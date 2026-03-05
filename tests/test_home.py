# import collections
# import collections.abc
#
# from pages import HomePage
#
# # 批量补全 Python 3.12 移除的 collections 根模块下的 ABC 类
# missing_attrs = [
#     'Mapping', 'MutableMapping', 'Sequence', 'MutableSequence',
#     'Set', 'MutableSet', 'Iterable', 'Iterator', 'Generator'
# ]
# for attr in missing_attrs:
#     if not hasattr(collections, attr):
#         setattr(collections, attr, getattr(collections.abc, attr))

import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#from appium.webdriver.common.action_chains import ActionChains
#from appium.webdriver.common.touch_action import TouchAction
import time
#from allure_commons.types import SeverityLevel

import allure

from pages import HomePage, CategoryPage
from utils.data_utils import DataUtils
import os
# 加载测试数据tes
current_dir=os.path.dirname(__file__)
test_home_data = DataUtils.load_excel(os.path.join(os.path.dirname(current_dir),"test_data/excel/test_home.xlsx"))

@pytest.fixture(scope="function")
def page_objects(driver):
    """初始化所有需要的Page对象，封装成字典供用例调用"""
    return {
        "category_page": CategoryPage(driver),
        "home_page": HomePage(driver)
    }

@allure.feature("UI交互测试")  # 大模块
class TestHomePage:



    @allure.story("服务按钮选择")  # 子功能
    @allure.severity(allure.severity_level.CRITICAL)  # 优先级
    @pytest.mark.parametrize("casename, parameter", test_home_data)
    def test_service_buttons(self,page_objects,casename, parameter):
        """测试服务按钮功能"""
        # 执行操作
        print(casename, parameter)
        home_page = page_objects["home_page"]
        with allure.step("点击服务按钮"):
            home_page.click_service_button()
        with allure.step("点击首页按钮"):
            home_page.click_home_button()




    @allure.story("分类按钮点击")  # 子功能
    def test_category_buttons(self,page_objects):
        """测试分类按钮功能"""
        # 执行操作
        home_page = page_objects["home_page"]
        with allure.step("点击分类按钮"):
            home_page.click_category()
        with allure.step("点击首页按钮"):
            home_page.click_home_button()




