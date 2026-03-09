from core.base_page import BasePage
from core.decorators import retry, retry_on_exception
from element.service_element import ServiceElement
from tenacity import retry, stop_after_attempt, wait_fixed


class ServicePage(BasePage):
    """服务"""
