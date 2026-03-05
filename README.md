# Appium 3.0 企业级测试框架

## 框架简介

这是一个基于 Appium 3.0 的企业级自动化测试框架，使用 POM (Page Object Model) 模式，支持 Android 平台的应用测试。

## 框架结构

```
appium3-enterprise-framework/
 ├── .env.dev                # 开发环境配置（Appium 端口、驱动版本等）
 ├── .env.test               # 测试环境配置
 ├── .env.prod               # 生产环境配置
 ├── pytest.ini              # pytest 全局配置
 ├── requirements.txt        # 依赖清单（指定 Appium 3.X 兼容版本）
 ├── README.md               # 框架使用文档
 ├── appium_config/          # Appium 3.X 专属配置
 │   ├── driver.yaml         # 驱动版本、启动参数配置
 │   └── server.yaml         # Appium Server 3.X 服务配置
 ├── config/                 # 业务配置
 │   ├── __init__.py
 │   ├── config_loader.py    # 配置加载器（统一解析环境变量/YAML）
 │   ├── app_config.py       # App 配置（包名、启动页、环境地址）
 │   └── device_config.py    # 设备配置（UDID、系统版本）
 ├── core/                   # 核心驱动层（Appium 3.X 适配）
 │   ├── __init__.py
 │   ├── driver_factory.py   # 驱动工厂（创建 3.X 驱动、管理服务）
 │   ├── base_page.py        # 页面基类（通用操作封装）
 │   ├── decorators.py       # 装饰器（重试、日志、截图）
 │   └── exceptions.py       # 自定义异常类
 ├── pages/                  # 页面层（PO 模式）
 │   ├── __init__.py
 │   ├── login_page.py       # 登录页
 │   ├── home_page.py        # 首页
 │   └── mine_page.py        # 我的页面
 ├── test_data/              # 测试数据
 │   ├── excel/              # Excel 数据文件
 │   └── yaml/               # YAML 数据文件
 ├── tests/                  # 测试用例层
 │   ├── __init__.py
 │   ├── conftest.py         # pytest 夹具（驱动初始化/销毁）
 │   ├── test_login.py       # 登录用例
 │   └── test_home.py        # 首页用例
 ├── utils/                  # 工具类
 │   ├── __init__.py
 │   ├── log_utils.py        # 日志工具（loguru 封装）
 │   ├── data_utils.py       # 数据解析工具（Excel/YAML）
 │   ├── screenshot_utils.py # 截图工具（嵌入 Allure 报告）
 │   └── driver_check.py     # Appium 3.X 驱动检查工具
 ├── reports/                # 测试报告
 │   ├── allure-results      # Allure 原始结果
 │   ├── allure-report       # Allure HTML 报告
 │   └── screenshots         # 失败截图
 └── logs/                   # 日志文件
     └── appium3_framework.log
```

## 核心适配点

1. **驱动管理**：Appium 3.X 需手动安装驱动，框架内置驱动检查 / 自动安装工具
2. **API 适配**：使用 AppiumOptions 替代旧 Capabilities，通过 AppiumService 管理服务生命周期
3. **依赖版本**：严格指定 appium-python-client≥3.3.0，确保与 Appium 3.X 兼容

## 企业级能力

1. **分层设计**：驱动层→页面层→用例层解耦，PO 模式提升复用性
2. **稳定性**：重试装饰器、显式等待、失败自动截图，解决 Appium 元素定位不稳定问题
3. **工程化**：多环境配置、数据驱动、并行执行、Allure 报告，满足大规模测试需求
4. **可扩展**：驱动工厂支持多平台（Android/iOS），页面基类可扩展 H5 / 小程序测试

## 快速开始

### 1. 安装依赖

```bash
pip install -r requirements.txt
```

### 2. 配置环境变量

根据测试环境选择对应的配置文件，例如开发环境：

```bash
cp .env.dev .env
```

### 3. 检查驱动

运行驱动检查工具，确保 Appium 和驱动已正确安装：

```bash
python -c "from utils.driver_check import DriverCheck; DriverCheck.run_full_check()"
```

### 4. 运行测试

使用 run_tests.py 脚本运行测试：

```bash
python run_tests.py
```

### 5. 查看报告

测试完成后，查看 Allure 报告：

```bash
allure serve ./reports/allure-results
```

## 编写测试用例

### 1. 创建页面类

在 `pages` 目录下创建页面类，继承自 `BasePage`，例如：

```python
from appium.webdriver.common.appiumby import AppiumBy
from core.base_page import BasePage
from core.decorators import retry, screenshot_on_failure

class HomePage(BasePage):
    """首页"""
    
    # 元素定位器
    MI_NEWS_BUTTON = (AppiumBy.XPATH, "//android.widget.TextView[@resource-id='com.xiaomi.shop:id/text' and @text='小米上新']")
    
    @retry()
    @screenshot_on_failure
    def click_mi_news(self):
        """点击小米上新按钮"""
        self.click(self.MI_NEWS_BUTTON)
```

### 2. 编写测试用例

在 `tests` 目录下创建测试用例文件，例如：

```python
import pytest
import allure
from pages.home_page import HomePage
from utils.log_utils import logger

@allure.feature("小米商城测试")
@allure.story("首页功能测试")
def test_mi_news_button(driver):
    """测试小米上新按钮功能"""
    logger.info("开始测试小米上新按钮功能")
    home_page = HomePage(driver)
    
    with allure.step("点击小米上新按钮"):
        home_page.click_mi_news()
    
    with allure.step("返回上一页"):
        home_page.back()
    
    logger.info("小米上新按钮功能测试完成")
```

## 配置说明

### 环境变量配置

- `.env.dev`：开发环境配置
- `.env.test`：测试环境配置
- `.env.prod`：生产环境配置

### Appium 配置

- `appium_config/driver.yaml`：驱动版本和启动参数配置
- `appium_config/server.yaml`：Appium Server 服务配置

### 业务配置

- `config/app_config.py`：应用配置（包名、启动页等）
- `config/device_config.py`：设备配置（UDID、系统版本等）

## 注意事项

1. 确保 Appium 3.0 已正确安装
2. 确保设备已通过 ADB 连接
3. 确保应用已安装在设备上
4. 运行测试前，先运行驱动检查工具
5. 如需修改配置，修改对应的环境变量文件

## 扩展建议

1. **添加 iOS 支持**：在 `driver_factory.py` 中添加 iOS 驱动支持
2. **添加 H5 测试**：在 `base_page.py` 中添加 WebView 切换功能
3. **添加数据驱动**：使用 `test_data` 目录下的 Excel 或 YAML 文件存储测试数据
4. **添加 CI/CD 集成**：配置 Jenkins 或 GitHub Actions 实现持续集成
5. **添加更多页面和测试用例**：根据应用功能扩展页面类和测试用例