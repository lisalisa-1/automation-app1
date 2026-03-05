# 首页页面类
from core.base_page import BasePage
from core.decorators import retry, retry_on_exception
from element.category_element import CategoryElement

class CategoryPage(BasePage):
    """首页"""



