import pytest
import allure
from unicodedata import category

from utils.data_utils import DataUtils
import os
# 加载测试数据tes
current_dir=os.path.dirname(__file__)
#test_home_data = DataUtils.load_excel(os.path.join(os.path.dirname(current_dir),"test_data/excel/test_home.xlsx"))
#test_data_dict = DataUtils.load_yaml(os.path.join(os.path.dirname(current_dir),"test_data/test_home.yaml"))
login_data = DataUtils.read_yaml(os.path.join(os.path.dirname(os.path.dirname(current_dir)),"test_data/module/test_home.yaml"))



@allure.feature("首页底部按钮功能")  # 大模块
class TestHomePage:

    #@pytest.mark.xfail
    @pytest.mark.run(order=1)
    @allure.story("底部功能按钮选择")  # 子功能
    @allure.severity(allure.severity_level.CRITICAL)  # 优先级
    #@pytest.mark.parametrize("casename", DataUtils.get_pytest_params(login_data["test_function_buttons"]))
    def test_function_buttons(self,page_factory):
        #初始化页面
        home_page = page_factory.get_page("home_page")
        my_page=page_factory.get_page("my_page")
        category_page=page_factory.get_page("category_page")
        """测试功能按钮功能"""
        # 执行操作
        with allure.step("点击服务按钮"):
            home_page.click_service_button()
        with allure.step("点击首页按钮"):
            home_page.click_home_button()
        with allure.step("点击分类按钮"):
            home_page.click_category_button()
            category_page.click_button_search_switcher()
            category_page.click_browser_back()

        with allure.step("点击我的按钮"):
            home_page.click_my_button()
            my_page.get_img_money()
            my_page.get_text_money()





