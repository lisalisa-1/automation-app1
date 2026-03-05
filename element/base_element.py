# 所有页面定位类的基类：存放公共元素定位符
from appium.webdriver.common.appiumby import AppiumBy


class BaseElement:
    """公共元素定位基类（所有页面定位类都继承此类）"""
    # 系统/全局公共元素
    BACK_BUTTON = (AppiumBy.XPATH, "//android.widget.ImageButton[@content-desc='返回']")  # 通用返回按钮
    TITLE_BAR = (AppiumBy.ID, "com.xiaomi.shop:id/title_bar")  # 通用标题栏
    LOADING_POPUP = (AppiumBy.ID, "com.xiaomi.shop:id/loading")  # 通用加载弹窗
    CLOSE_POPUP_BUTTON = (AppiumBy.ID, "com.xiaomi.shop:id/close_btn")  # 通用弹窗关闭按钮

    # App全局公共元素（小米商城通用）
    APP_LOGO = (AppiumBy.ID, "com.xiaomi.shop:id/app_logo")  # 商城logo
    TOAST_MESSAGE = (AppiumBy.XPATH, "//android.widget.Toast")  # 通用提示语