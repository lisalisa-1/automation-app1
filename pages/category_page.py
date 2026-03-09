from core.base_page import BasePage
from core.decorators import retry, retry_on_exception
from element.category_element import CategoryElement

class CategoryPage(BasePage):
    """分类页"""
    def __init__(self, driver):
        super().__init__(driver)
        self.element = CategoryElement()

    def click_search_switcher(self):
        """点击搜索切换器"""
        self.click(self.element.SEARCH_SWITCHER)

    def click_button_search_switcher(self):
        """点击搜索切换器"""
        self.click(self.element.BUTTON_SEARCH_SWITCHER)

    def input_search_keyword(self, keyword):
        """输入搜索关键词"""
        self.send_keys(self.element.INPUT_SEARCH, keyword)

    def get_category_list(self):
        """获取分类列表"""
        return self.find_element(self.element.CATEGORY_LIST)
    def get_search_result(self):
        """获取搜索结果"""
        return self.find_elements(self.element.SEARCH_RESULT)

    def get_list_goods(self):
        """获取商品列表"""
        return self.find_elements(self.element.LIST_GOODS)

