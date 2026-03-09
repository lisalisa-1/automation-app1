# 集中管理所有配置，避免硬编码
class Config:
    # 超时配置
    IMPLICITLY_WAIT = 10  # 隐式等待
    EXPLICITLY_WAIT = 10  # 显式等待

    # 报告配置
    ALLURE_RESULTS = "./reports/allure-results"
    ALLURE_HTML = "./reports/allure-report"
    SCREENSHOT_DIR = "./reports/screenshots/"