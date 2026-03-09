import subprocess
import time

from config.config_loader import Appium3Settings
from loguru import logger

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
        cmd = 'appium driver list --installed'
        result = subprocess.run(
            cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            shell=True,  # Windows 下必须加，因为appium是cmd脚本
            encoding='utf-8'  # 可选：指定编码，避免中文乱码
        )

        logger.info(f"已安装驱动列表：{result.stdout.strip()}")
        app3_setting=Appium3Settings()
        if app3_setting.driver_name not in result.stdout:
            # 自动安装驱动
            install_cmd = f"appium driver install {app3_setting.driver_name}@{app3_setting.driver_version}"
            logger.info(f"🔧 执行安装命令：{install_cmd}")
            subprocess.run(install_cmd.split(), check=True)
            logger.info(f"✅ 自动安装驱动：{app3_setting.driver_name}@{app3_setting.driver_version}")
        else:
            logger.info(f"✅ 驱动 {app3_setting.driver_name} 已安装")
    except Exception as e:
        raise RuntimeError(f"驱动检查/安装失败：{str(e)}")