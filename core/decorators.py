import logging
from functools import wraps
from tenacity import retry, stop_after_attempt, wait_fixed, retry_if_exception_type
from selenium.common.exceptions import NoSuchElementException, TimeoutException

logger = logging.getLogger(__name__)

def retry_on_exception(max_attempts: int = 2, delay: int = 1):
    """
    异常重试装饰器：适配 Appium 3.X 元素定位不稳定问题
    :param max_attempts: 最大重试次数
    :param delay: 重试间隔（秒）
    """
    def decorator(func):
        @wraps(func)
        @retry(
            stop=stop_after_attempt(max_attempts),
            wait=wait_fixed(delay),
            retry=retry_if_exception_type((NoSuchElementException, TimeoutException)),
            reraise=True
        )
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                #logger.warning(f"执行 {func.__name__} 失败，第 {wrapper.retry.statistics['attempt_number']} 次重试...")
                logger.warning(f"执行 {func.__name__} 失败，第 1 次重试...")
                raise
        return wrapper
    return decorator