import pytest
from utils.log_utils import init_logger
from loguru import logger
from config.config_loader import load_env
from core.driver_factory import Appium3DriverFactory

import platform
import sys
from pathlib import Path
from core import PageFactory
from utils import ScreenshotUtils
# 初始化日志

init_logger()

# 自定义命令行参数：指定测试环境
def pytest_addoption(parser):
    parser.addoption("--env", action="store", default="test",choices=["dev", "test", "prod"], help="测试环境：dev/test/prod")
    logger.info("添加命令行参数 --env")

# 环境参数夹具
@pytest.fixture(scope="session")
def env(request):
    logger.info(f"当前环境：{request.config.getoption('--env')}")
    return request.config.getoption("--env")

# Appium 3.X 驱动夹具（会话级）
@pytest.fixture(scope="session")
def driver(env):

    """全局驱动：每个测试会话只创建一次"""
    logger.info(f"加载环境配置：{env}")
    load_env(env)  # 加载指定环境配置
    driver_factory = Appium3DriverFactory()
    driver = driver_factory.create_driver()
    yield driver
    driver_factory.quit()

# Allure 报告配置
def pytest_configure(config):
    allure_results_dir = config.getoption("--alluredir") or "./allure-results"
    # 确保目录存在（不存在则创建）
    Path(allure_results_dir).mkdir(parents=True, exist_ok=True)

    # 2. 定义要设置的环境元数据（键值对形式，值需为字符串）
    environment_data = {
        # 系统基础信息
        "Python 版本": sys.version.split()[0],
        "操作系统": f"{platform.system()} {platform.release()}",
        "架构": platform.machine(),
        "Pytest 版本": '3.12',
        # 自定义业务信息
        "项目名称": "XX自动化测试项目",
        "项目版本": "v2.6.0",
        "测试环境": "预发布环境",
        "接口域名": "https://pre-api.xxx.com",
        "数据库地址": "192.168.1.100:3306"
    }

    # 3. 生成 environment.properties 文件（allure2.15+ 核心）
    env_file_path = Path(allure_results_dir) / "environment.properties"
    with open(env_file_path, "w", encoding="utf-8") as f:
        for key, value in environment_data.items():
            # 格式要求：key=value，注意编码和特殊字符转义
            f.write(f"{key}={value}\n")

    # ========== 可选：注册 allure 标记（避免警告） ==========
    config.addinivalue_line("markers", "allure.feature: 功能模块标记")
    config.addinivalue_line("markers", "allure.story: 子功能标记")
    config.addinivalue_line("markers", "allure.severity: 优先级标记")
# 用例失败自动截图
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    logger.info(f"\n钩子触发 → 用例：{item.nodeid} | 阶段：{rep.when} | 是否失败：{rep.failed}")

    if rep.when == "call" and rep.failed:
        try:
            driver = item.funcargs["driver"]
            ScreenshotUtils.capture(driver, f"test_failed_")
        except Exception as e:
            logger.error(f"截图失败：{str(e)}")

@pytest.fixture(scope="function",autouse=True)
def page_factory(driver):
    """Page工厂Fixture"""
    return PageFactory(driver)

