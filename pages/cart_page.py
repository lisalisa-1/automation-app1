# 首页页面类
from core.base_page import BasePage
from core.decorators import retry, retry_on_exception
from element.cart_element import CartElement
from tenacity import retry, stop_after_attempt, wait_fixed


class CartPage(BasePage):
    """购物车"""
