# 核心驱动层包初始化文件
from .driver_factory import Appium3DriverFactory
from .base_page import BasePage
#from .decorators import retry, screenshot_on_failure
from .exceptions import AppiumFrameworkError
from .page_factory import PageFactory

#__all__ = ['Appium3DriverFactory', 'BasePage', 'retry', 'screenshot_on_failure', 'AppiumFrameworkError']
__all__ = ['Appium3DriverFactory', 'BasePage',  'AppiumFrameworkError', 'PageFactory']
