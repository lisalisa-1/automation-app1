import subprocess
import logging
from config.config_loader import appium3_cfg

logger = logging.getLogger(__name__)

def check_appium3_env():
    """检查 Appium 3.X 环境是否符合要求"""
    # 1. 检查 Appium 版本
    try:
        result = subprocess.run(
            ["appium", "--version"],
            capture_output=True,
            text=True,
            check=True,
            shell=True
        )
        version = result.stdout.strip()
        if not version.startswith("3."):
            raise RuntimeError(f"Appium 版本要求 3.X，当前为 {version}")
        logger.info(f"✅ Appium 版本校验通过：{version}")
    except Exception as e:
        raise RuntimeError(f"Appium 环境检查失败：{str(e)}")

    # 2. 检查驱动是否安装
    try:
        result = subprocess.run(
            ["appium", "driver", "list", "--installed"],
            capture_output=True,
            text=True,
            check=True,
            shell=True
        )
        # if appium3_cfg.driver_name not in result.stdout:
        #     # 自动安装驱动
        #     install_cmd = f"appium driver install {appium3_cfg.driver_name}@{appium3_cfg.driver_version}"
        #     subprocess.run(install_cmd.split(), check=True)
        #     logger.info(f"✅ 自动安装驱动：{appium3_cfg.driver_name}@{appium3_cfg.driver_version}")
        # else:
        #     logger.info(f"✅ 驱动 {appium3_cfg.driver_name} 已安装")
    except Exception as e:
        raise RuntimeError(f"驱动检查/安装失败：{str(e)}")