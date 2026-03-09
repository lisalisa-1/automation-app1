from core.base_page import BasePage
from core.decorators import retry, retry_on_exception
from element.my_element import MyElement
from tenacity import retry, stop_after_attempt, wait_fixed


class MyPage(BasePage):
    """我的"""
    def click_member_code(self):
        """点击会员中心"""
        self.click(MyElement.MY_Member_Code)

    def get_img_money(self):
        """获取钱包图标"""
        return self.find_element(MyElement.IMG_MONEY)

    def get_text_money(self):
        return self.find_element(MyElement.TEXT_MONEY)
        """获取钱包文本"""
