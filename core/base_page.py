import logging
from appium.webdriver import Remote
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.screenshot_utils import ScreenshotUtils

logger = logging.getLogger(__name__)


class BasePage:
    """页面基类：封装 Appium 3.X 通用操作"""

    def __init__(self, driver: Remote):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15, poll_frequency=0.5)  # 显式等待

    def find_element(self, locator: tuple):
        """查找元素（3.X 兼容定位方式）"""
        by, value = locator
        try:
            element = self.wait.until(EC.presence_of_element_located((by, value)))
            logger.debug(f"找到元素：{by}={value}")
            return element
        except (NoSuchElementException, TimeoutException):
            ScreenshotUtils.capture(self.driver, f"element_not_found_{value}")
            raise NoSuchElementException(f"元素定位失败：{by}={value}")

    def click(self, locator: tuple):
        """点击元素"""
        self.find_element(locator).click()
        logger.debug(f"点击元素：{locator}")

    def send_keys(self, locator: tuple, text: str):
        """输入文本"""
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)
        logger.debug(f"输入文本：{text} 到元素 {locator}")

    def get_text(self, locator: tuple) -> str:
        """获取元素文本"""
        text = self.find_element(locator).text
        logger.debug(f"获取元素文本：{text}")
        return text

    def swipe_up(self, duration: int = 500):
        """向上滑动（3.X 兼容 swipe API）"""
        size = self.driver.get_window_size()
        self.driver.swipe(
            start_x=size["width"] / 2,
            start_y=size["height"] * 0.8,
            end_x=size["width"] / 2,
            end_y=size["height"] * 0.2,
            duration=duration
        )
        logger.debug("执行向上滑动操作")

    def switch_context(self, context: str):
        """切换上下文（原生/H5，3.X 兼容）"""
        self.driver.switch_to.context(context)
        logger.debug(f"切换上下文到：{context}")

    def get_current_activity(self) -> str:
        """获取当前 Activity（Android）"""
        return self.driver.current_activity