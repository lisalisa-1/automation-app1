# common/test_base.py  基础测试类/公共方法
import pytest
from pages.my_page import MyPage

class BaseTest:
    """基础测试类：封装所有通用逻辑"""

    # 通用前置：比如登录、初始化测试环境
    # def setup_method(self):
    #     self.token = self.login("test_user", "123456")  # 通用登录逻辑

    # 抽离通用方法：供其他用例调用
    def login(self, username, password,page_factory=None,):
        """通用登录逻辑（复用自登录测试类）"""
        # 实际项目中替换为真实的登录接口/操作
        my_page = page_factory.get_page("my_page")

        print(f"登录：{username}/{password}")
        my_page.click_member_code()

        return "fake_token_123"

    def create_order(self, goods_id, num):
        """创建订单逻辑（复用自订单测试类）"""
        print(f"创建订单：商品{goods_id}，数量{num}，token={self.token}")
        return {"order_id": f"order_{goods_id}_{num}", "status": "created"}

    def pay_order(self, order_id):
        """支付订单逻辑（复用自支付测试类）"""
        print(f"支付订单：{order_id}")
        return {"order_id": order_id, "status": "paid"}
    def add_cart(self, goods_id, num):
        """添加购物车逻辑（复用自购物车测试类）"""
        print(f"添加购物车：商品{goods_id}，数量{num}，token={self.token}")
        return {"goods_id": goods_id, "num": num, "status": "added"}
