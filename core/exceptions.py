# 自定义异常类


class AppiumFrameworkError(Exception):
    """Appium框架基础异常"""
    pass


class DriverCreationError(AppiumFrameworkError):
    """驱动创建异常"""
    pass


class ElementNotFoundException(AppiumFrameworkError):
    """元素未找到异常"""
    pass


class TimeoutException(AppiumFrameworkError):
    """超时异常"""
    pass


class TestFailureError(AppiumFrameworkError):
    """测试失败异常"""
    pass