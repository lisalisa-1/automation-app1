
# 项目入口文件（如 conftest.py、main.py）
import collections
import collections.abc
# 必须放在所有导入的最前面！

# # 批量补全 Python 3.12 移除的 collections 根模块下的 ABC 类
# missing_attrs = [
#     'Mapping', 'MutableMapping', 'Sequence', 'MutableSequence',
#     'Set', 'MutableSet', 'Iterable', 'Iterator', 'Generator'
# ]
# for attr in missing_attrs:
#     if not hasattr(collections, attr):
#         setattr(collections, attr, getattr(collections.abc, attr))# 给 collections 补全 Mapping 属性，兼容旧库
# if not hasattr(collections, 'Mapping'):
#     collections.Mapping = collections.abc.Mapping


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
    check_result = check_appium3_env
    
    if not check_result:
        logger.error("驱动检查失败，测试无法运行")
        return
    
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
    os.system('allure generate ./reports/allure-results -o ./reports/allure-report --clean --encoding=utf-8  ')
    
    # 查看报告
    logger.info("查看Allure报告...")
    os.system('allure serve ./reports/allure-results')
    
    logger.info("测试完成！报告已生成在 reports/allure-report 目录中")


if __name__ == "__main__":
    run_tests()