# 首页页面类
from core.base_page import BasePage
from core.decorators import retry, retry_on_exception
from element.home_element import HomeElement
from tenacity import retry, stop_after_attempt, wait_fixed


class HomePage(BasePage):
    """首页"""


    @retry_on_exception(max_attempts=1)
    def click_home_button(self):
        """点击首页按钮"""
        self.click(HomeElement.HOME_BUTTON)

    @retry(
        stop=stop_after_attempt(1),  # 最多重试3次
        wait=wait_fixed(0)  # 每次重试间隔2秒
    )
    def click_category_button(self):
        """点击分类按钮"""
        self.click(HomeElement.CATEGORY_BUTTON)
    
    @retry()
    def click_my_button(self):
        """点击我的按钮"""
        self.click(HomeElement.MINE_BUTTON)


    def click_service_button(self):
        """点击服务按钮"""
        self.click(HomeElement.SERVICE_BUTTON)

    def click_cart_button(self):
        """点击购物车按钮"""
        self.click(HomeElement.CART_BUTTON)



