from appium.webdriver.common.appiumby import AppiumBy
from element.base_element import BaseElement

class GoodsElement(BaseElement):
    TEXT_GOODS_PRICE = (AppiumBy.XPATH, "//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[1]/android.view.ViewGroup")
    BUTTON_ADD_CART = (AppiumBy.XPATH, "//android.widget.TextView[@text='加入购物车']")
