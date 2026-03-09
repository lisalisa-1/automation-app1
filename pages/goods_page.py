from core.base_page import BasePage
from core.decorators import retry, retry_on_exception
from element.goods_element import GoodsElement
from element.home_element import HomeElement
from tenacity import retry, stop_after_attempt, wait_fixed


class GoodsPage(BasePage):
    """首页"""


    def get_text_goods_price(self):
        """获取商品价格"""
        return self.find_element(GoodsElement.TEXT_GOODS_PRICE)

    def click_button_add_cart(self):
        """点击加入购物车按钮"""
        self.click(GoodsElement.BUTTON_ADD_CART)