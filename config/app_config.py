# 应用配置
import os


class AppConfig:
    """应用配置"""
    
    # 应用信息
    APP_PACKAGE = os.environ.get('APP_PACKAGE', 'com.xiaomi.shop')
    APP_ACTIVITY = os.environ.get('APP_ACTIVITY', 'com.xiaomi.shop2.activity.MainActivity')
    
    # 测试环境
    TEST_ENV = os.environ.get('TEST_ENV', 'dev')
    BASE_URL = os.environ.get('BASE_URL', 'http://dev-api.example.com')
    
    # 等待时间
    IMPLICIT_WAIT = 10
    EXPLICIT_WAIT = 20
    
    # 重试次数
    RETRY_COUNT = 3
    RETRY_DELAY = 2