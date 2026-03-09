# 分类页定位类：继承公共定位基类，新增分类页专属定位符
from appium.webdriver.common.appiumby import AppiumBy
from element.base_element import BaseElement

class CategoryElement(BaseElement):
    """分类页元素定位类（继承公共定位基类）"""
    # 分类页专属元素（新增）
    CATEGORY_PAGE_FLAG = (AppiumBy.ID, "com.xiaomi.shop.plugin.homepage:id/auto_fill_img")  # 分类页标识
    ELECTRONIC_CATEGORY = (AppiumBy.XPATH, "//android.widget.TextView[@text='电子产品']")    # 电子产品分类
    CLOTHING_CATEGORY = (AppiumBy.XPATH, "//android.widget.TextView[@text='服饰']")          # 服饰分类
    CATEGORY_BACK_BUTTON = (AppiumBy.ID, "com.xiaomi.shop:id/back_btn")
    BUTTON_SEARCH_SWITCHER = (AppiumBy.ID, "com.xiaomi.shop.plugin.homepage:id/fragment_search_view")
    INPUT_SEARCH= (AppiumBy.ID, "com.xiaomi.shop:id/input")

    CATEGORY_LIST=(AppiumBy.XPATH, '//android.widget.ScrollView[@resource-id="com.xiaomi.shop.plugin.homepage:id/verticalIndicator_category"]/android.widget.LinearLayout')
    SEARCH_RESULT=(AppiumBy.XPATH, '//android.widget.TextView[@resource-id="com.xiaomi.shop2.plugin.search:id/word" ]')
    LIST_GOODS=(AppiumBy.XPATH, '(//android.widget.LinearLayout[@resource-id="com.xiaomi.shop.plugin.homepage:id/listitem_category_group_item_cate_rootview"])')
