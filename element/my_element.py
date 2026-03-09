from appium.webdriver.common.appiumby import AppiumBy
from element.base_element import BaseElement

class MyElement(BaseElement):
    """我的元素定位类（继承公共定位基类）"""
    MY_Member_Code = (AppiumBy.ID, "com.xiaomi.shop.plugin.homepage:id/tv_member_code")
    IMG_MONEY=(AppiumBy.ID, "com.xiaomi.shop.plugin.homepage:id/assets_item_top_icon")
    TEXT_MONEY=(AppiumBy.XPATH, "//android.widget.TextView[@resource-id='com.xiaomi.shop.plugin.homepage:id/assets_item_text' and @text='钱包']")
