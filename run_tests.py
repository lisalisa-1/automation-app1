
# 项目入口文件（如 conftest.py、main.py）
# 运行测试脚本
import os
import pytest
from utils.driver_check import check_appium3_env
from utils.log_utils import logger

print("当前文件："+__file__)

def run_tests():
    """运行测试并生成Allure报告"""
    # 运行驱动检查
    logger.info("开始运行驱动检查...")
    #check_result = check_appium3_env()
    
    # 清除之前的测试结果
    allure_results_dir = os.path.join(os.getcwd(), "reports", "allure-results")
    if os.path.exists(allure_results_dir):
        for file in os.listdir(allure_results_dir):
            os.remove(os.path.join(allure_results_dir, file))

    # 运行测试
    logger.info("开始运行测试...")
    pytest.main(["tests/", "--env=test", "--alluredir=./reports/allure-results","--clean-alluredir"])
    
    # 生成Allure报告
    logger.info("生成Allure报告...")
    os.system('allure generate ./reports/allure-results -o ./reports/allure-report --clean --encoding=utf-8')
    
    # 查看报告
    logger.info("查看Allure报告...")
    os.system('allure serve ./reports/allure-results')
    
    logger.info("测试完成！报告已生成在 reports/allure-report 目录中")


if __name__ == "__main__":
    run_tests()