import pytest
import allure
from utils.data_utils import DataUtils
import os
# 加载测试数据tes
current_dir=os.path.dirname(__file__)
#test_home_data = DataUtils.load_excel(os.path.join(os.path.dirname(current_dir),"test_data/excel/test_home.xlsx"))
#test_data_dict = DataUtils.load_yaml(os.path.join(os.path.dirname(current_dir),"test_data/test_home.yaml"))
login_data = DataUtils.read_yaml(os.path.join(os.path.dirname(os.path.dirname(current_dir)),"test_data/module/test_category.yaml"))



@allure.feature("分类功能模块")  # 大模块
class TestCategoryPage:


    #@pytest.mark.xfail
    @pytest.mark.run(order=1)
    @allure.story("分类搜索功能")  # 子功能
    @allure.severity(allure.severity_level.CRITICAL)  # 优先级
    @pytest.mark.parametrize("casename", DataUtils.get_pytest_params(login_data["test_category_search"]))
    def test_category_search(self,casename,page_factory):

        home_page=page_factory.get_page("home_page")
        home_page.click_category_button()

        """测试分类搜索功能"""
        category_page=page_factory.get_page("category_page")
        # 执行操作
        with allure.step("点击搜索切换器"):
            category_page.click_button_search_switcher()
        with allure.step("输入搜索关键词"):
            category_page.input_search_keyword(casename["category_keyword"])
        with allure.step("获取搜索结果"):
            search_result=category_page.get_search_result()
            assert len(search_result) > 0, "搜索结果为空"
            for item in search_result:
                assert casename["category_keyword"] in item.text, f"搜索结果中未包含关键词：{casename['category_keyword']}"


