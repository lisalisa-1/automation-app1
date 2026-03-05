import logging
from appium import webdriver
from appium.options.common import AppiumOptions  # 3.X 标准化 Options
from appium.webdriver.appium_service import AppiumService  # 3.X 服务管理
from config.config_loader import appium3_cfg, app_cfg, device_cfg
from utils.driver_check import check_appium3_env

logger = logging.getLogger(__name__)


class Appium3DriverFactory:
    """Appium 3.X 驱动工厂：负责驱动创建、服务启停"""

    def __init__(self):
        self.service = AppiumService()
        self.driver = None

    def start_server(self):
        """启动 Appium 3.X 服务（适配 3.X CLI 命令）"""
        # 前置检查：Appium 3.X 环境和驱动
        check_appium3_env()

        # 3.X 启动参数
        server_args = [
            "--host", appium3_cfg.server_host,
            "--port", str(appium3_cfg.server_port),
            "--log-level", appium3_cfg.log_level,
  #          "--driver-executable-dir", "./.appium/drivers",  # 3.X 驱动目录
            "--session-override"  # 覆盖已有会话
        ]

        # # 启动服务
        # try:
        #     if not self.service.is_running:
        #         self.service.start(args=server_args)
        #         service_url=f"{appium3_cfg.server_host}:{appium3_cfg.server_port}"
        #         logger.info(f"✅ Appium 3.X 服务启动成功：{service_url}")
        # except Exception as e:
        #     logger.error(f"❌ Appium 3.X 服务启动失败：{str(e)}")
        #     raise

    def create_driver(self) -> webdriver.Remote:
        """创建 Appium 3.X 驱动（使用标准化 Options）"""
        # 1. 启动服务
        self.start_server()

        # 2. 构建 3.X Options（替代旧的 desired_capabilities）
        options = AppiumOptions()

        # 核心 Capability（3.X 必须配置）
        options.set_capability("platformName", device_cfg.platform_name)
        options.set_capability("platformVersion", device_cfg.platform_version)
        options.set_capability("deviceName", device_cfg.device_name)
        options.set_capability("udid", device_cfg.udid)
        options.set_capability("appium:driverName", appium3_cfg.driver_name)  # 3.X 关键：指定驱动
        options.set_capability("appium:noReset", True)  # 不重置应用
        options.set_capability("appium:newCommandTimeout", 30)  # 超时时间

        # 平台专属配置
        if device_cfg.platform_name.lower() == "android":
            options.set_capability("appPackage", app_cfg.package)
            options.set_capability("appActivity", app_cfg.activity)
            options.set_capability("unicodeKeyboard", True)  # 支持中文
            options.set_capability("resetKeyboard", True)
            options.set_capability('automationName', 'UiAutomator2')  # 自动化引擎（安卓用 UiAutomator2，iOS 用 XCUITest）

        elif device_cfg.platform_name.lower() == "ios":
            options.set_capability("appium:bundleId", app_cfg.package)
            options.set_capability("appium:automationName", "XCUITest")



        # 3. 创建驱动会话（3.X 会话逻辑）
        try:
            self.driver = webdriver.Remote(
                command_executor=f"{appium3_cfg.server_host}:{appium3_cfg.server_port}",
                options=options  # 3.X 必须用 options，废弃 desired_capabilities
            )
            self.driver.implicitly_wait(10)  # 隐式等待
            logger.info(f"✅ Appium 3.X 驱动创建成功（{device_cfg.platform_name}）")
            return self.driver
        except Exception as e:
            logger.error(f"❌ 驱动创建失败：{str(e)}")
            self.stop_server()
            raise

    def stop_server(self):
        """停止 Appium 3.X 服务"""
        if self.service.is_running:
            self.service.stop()
            logger.info("✅ Appium 3.X 服务已停止")

    def quit(self):
        """退出驱动 + 停止服务（资源释放）"""
        if self.driver:
            self.driver.quit()
            logger.info("✅ 驱动已退出")
        self.stop_server()