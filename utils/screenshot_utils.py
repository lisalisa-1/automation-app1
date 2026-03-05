
import os
import time
import traceback
from typing import Optional
from allure_commons.types import AttachmentType
import allure

class ScreenshotUtils:
    """Allure 2.15 专用截图工具类"""

    # 默认配置（可全局修改）
    DEFAULT_SCREENSHOT_DIR = os.path.join(os.getcwd(), "reports", "screenshots")
    DEFAULT_EXTENSION = "png"

    @classmethod
    def _get_unique_filename(cls, name: str, suffix: str = "") -> str:
        """
        生成唯一文件名（避免重复）
        :param name: 基础名称
        :param suffix: 后缀（如 full/error）
        :return: 唯一文件名（包含时间戳）
        """
        timestamp = time.strftime("%Y%m%d_%H%M%S", time.localtime())
        suffix_part = f"_{suffix}" if suffix else ""
        return f"{name}{suffix_part}_{timestamp}.{cls.DEFAULT_EXTENSION}"

    @classmethod
    def _ensure_dir(cls, dir_path: str) -> None:
        """确保目录存在，不存在则创建"""
        os.makedirs(dir_path, exist_ok=True)

    @classmethod
    def capture(
            cls,
            driver,
            name: str,
            screenshot_dir: Optional[str] = None,
            add_to_allure: bool = True
    ) -> Optional[str]:
        """
        核心截图方法（适配 Allure 2.15）
        :param driver: WebDriver/Appium Driver 实例
        :param name: 截图基础名称（如"首页"）
        :param screenshot_dir: 自定义截图目录（默认使用 DEFAULT_SCREENSHOT_DIR）
        :param add_to_allure: 是否添加到 Allure 报告（默认是）
        :return: 截图文件路径（失败返回 None）
        """
        # 确定最终截图目录
        target_dir = screenshot_dir or cls.DEFAULT_SCREENSHOT_DIR
        cls._ensure_dir(target_dir)

        # 生成唯一文件名和路径
        filename = cls._get_unique_filename(name)
        screenshot_path = os.path.join(target_dir, filename)

        try:
            # 执行截图（WebDriver/Appium 通用方法）
            driver.save_screenshot(screenshot_path)
            print(f"✅ 截图成功：{screenshot_path}")

            # 适配 Allure 2.15：添加附件到报告
            if add_to_allure:
                allure.attach.file(
                    source=screenshot_path,
                    name=name,
                    attachment_type=AttachmentType.PNG,
                    extension=cls.DEFAULT_EXTENSION
                )

            return screenshot_path

        except Exception as e:
            # 异常处理：记录日志并添加错误信息到 Allure
            error_msg = f"❌ 截图失败（{name}）：{str(e)}\n{traceback.format_exc()}"
            print(error_msg)

            # 把错误信息添加到 Allure 报告
            allure.attach(
                body=error_msg,
                name=f"{name}_截图失败信息",
                attachment_type=AttachmentType.TEXT
            )
            return None

    @classmethod
    def capture_full_screen(
            cls,
            driver,
            name: str,
            screenshot_dir: Optional[str] = None,
            add_to_allure: bool = True
    ) -> Optional[str]:
        """
        全屏截图（兼容 get_screenshot_as_file 方法）
        :param driver: WebDriver/Appium Driver 实例
        :param name: 截图基础名称
        :param screenshot_dir: 自定义截图目录
        :param add_to_allure: 是否添加到 Allure 报告
        :return: 截图文件路径
        """
        target_dir = screenshot_dir or cls.DEFAULT_SCREENSHOT_DIR
        cls._ensure_dir(target_dir)

        # 生成带 full 后缀的唯一文件名
        filename = cls._get_unique_filename(name, suffix="full")
        screenshot_path = os.path.join(target_dir, filename)

        try:
            # 全屏截图（等价于原 get_screenshot_as_file 逻辑）
            driver.get_screenshot_as_file(screenshot_path)
            print(f"✅ 全屏截图成功：{screenshot_path}")

            if add_to_allure:
                allure.attach.file(
                    source=screenshot_path,
                    name=f"{name}_全屏",
                    attachment_type=AttachmentType.PNG,
                    extension=cls.DEFAULT_EXTENSION
                )

            return screenshot_path

        except Exception as e:
            error_msg = f"❌ 全屏截图失败（{name}）：{str(e)}\n{traceback.format_exc()}"
            print(error_msg)
            allure.attach(
                body=error_msg,
                name=f"{name}_全屏截图失败信息",
                attachment_type=AttachmentType.TEXT
            )
            return None

    @classmethod
    def capture_on_failure(cls, driver, test_name: str):
        """
        测试失败时的专用截图方法（建议结合 pytest/unitest 异常捕获使用）
        :param driver: WebDriver/Appium Driver 实例
        :param test_name: 测试用例名称
        """
        cls.capture(driver, name=f"{test_name}_失败截图", add_to_allure=True)
@staticmethod
def take_screenshot(driver, name):
    """截图并添加到Allure报告"""
    # 确保截图目录存在
    screenshot_dir = os.path.join(os.getcwd(), "reports", "screenshots")
    os.makedirs(screenshot_dir, exist_ok=True)

    # 截图路径
    screenshot_path = os.path.join(screenshot_dir, f"{name}.png")

    # 执行截图
    driver.save_screenshot(screenshot_path)

    # 添加到Allure报告（使用更通用的方式）
    with open(screenshot_path, 'rb') as f:
        allure.attach(
            f.read(),
            name=name,
            attachment_type=AttachmentType.PNG
        )

    return screenshot_path

@staticmethod
def take_full_screenshot(driver, name):
    """截取全屏并添加到Allure报告"""
    # 确保截图目录存在
    screenshot_dir = os.path.join(os.getcwd(), "reports", "screenshots")
    os.makedirs(screenshot_dir, exist_ok=True)

    # 截图路径
    screenshot_path = os.path.join(screenshot_dir, f"{name}_full.png")

    # 执行全屏截图
    driver.get_screenshot_as_file(screenshot_path)

    # 添加到Allure报告（使用更通用的方式）
    with open(screenshot_path, 'rb') as f:
        allure.attach(
            f.read(),
            name=f"{name}_full",
            attachment_type=AttachmentType.PNG
        )

    return screenshot_path