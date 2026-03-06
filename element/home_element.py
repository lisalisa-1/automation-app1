# 首页定位类：继承公共定位基类，新增首页专属定位符
from appium.webdriver.common.appiumby import AppiumBy
from element.base_element import BaseElement

class HomeElement(BaseElement):
    """首页元素定位类（继承公共定位基类）"""
    # 首页专属元素（新增）
    MI_NEW_PRODUCT = (AppiumBy.XPATH, "//android.widget.TextView[@resource-id='com.xiaomi.shop:id/text' and @text='小米上新']")
    CATEGORY_BUTTON = (AppiumBy.ID, "com.xiaomi.shop.plugin.homepage:id/main_bottom_category1") #分类
    SEARCH_BOX = (AppiumBy.ID, "com.xiaomi.shop:id/search_input")                      # 首页搜索框
    SERVICE_BUTTON = (AppiumBy.ID, "com.xiaomi.shop.plugin.homepage:id/main_bottom_discovery")                      # 首页搜索按钮
    CART_BUTTON = (AppiumBy.ID, "com.xiaomi.shop.plugin.homepage:id/main_bottom_cart") # 首页购物车按钮
    HOME_BUTTON = (AppiumBy.ID, "com.xiaomi.shop.plugin.homepage:id/main_bottom_home") # 首页底部首页按钮
    MINE_BUTTON = (AppiumBy.ID, "com.xiaomi.shop.plugin.homepage:id/main_bottom_mine") # 首页底部我的按钮
