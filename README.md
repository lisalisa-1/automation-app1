# Appium 3.0 企业级测试框架

## 项目简介

本项目是基于 Appium 3.0 的企业级移动应用自动化测试框架，采用 POM (Page Object Model) 设计模式，结合 Pytest 测试框架和 Allure 报告系统，为小米商城等移动应用提供高效、稳定的自动化测试方案。

## 技术栈

- **Appium 3.0**：新一代移动应用自动化测试框架
- **Pytest**：强大的 Python 测试框架，支持参数化、fixture 等特性
- **Allure**：生成美观、详细的测试报告
- **POM 设计模式**：页面元素与操作分离，提高代码复用性
- **多环境配置**：支持开发、测试、生产环境切换
- **数据驱动**：支持 Excel 和 YAML 数据文件
- **日志管理**：使用 Loguru 实现结构化日志

## 项目结构

```
automation-app1/
├── config/           # 配置管理
├── core/             # 核心功能
├── element/          # 页面元素定位
├── pages/            # 页面类
├── reports/          # 测试报告
├── test_data/        # 测试数据
├── tests/            # 测试用例
├── utils/            # 工具类
├── .env.*            # 环境配置文件
├── conftest.py       # Pytest 配置
├── pytest.ini        # Pytest 配置文件
├── requirements.txt  # 依赖包
├── run_tests.py      # 测试执行入口
└── README.md         # 项目说明
```

### 目录说明

- **config/**：配置管理，包含环境变量加载和配置模型
- **core/**：核心功能，包含驱动管理、页面工厂等
- **element/**：页面元素定位，按页面分类管理元素
- **pages/**：页面类，封装页面操作和业务逻辑
- **reports/**：测试报告，包含 Allure 结果和截图
- **test_data/**：测试数据，支持 Excel 和 YAML 格式
- **tests/**：测试用例，按模块和场景分类
- **utils/**：工具类，包含数据解析、截图、日志等

## 环境配置

### 1. 安装依赖

```bash
pip install -r requirements.txt
```

### 2. 配置 Appium 3.0

```bash
# 安装 Appium 3.0
npm install -g appium

# 安装 UIAutomator2 驱动
appium driver install uiautomator2
```

### 3. 配置环境变量

在项目根目录创建环境配置文件：

- **.env.dev**：开发环境配置
- **.env.test**：测试环境配置
- **.env.prod**：生产环境配置

示例配置（.env.test）：

```
# App 配置
APP_PACKAGE=com.xiaomi.shop
APP_ACTIVITY=com.xiaomi.shop.activity.MainActivity
APP_APP_PATH=path/to/app.apk
APP_BASE_URL=https://api.mi.com

# 设备配置
DEVICE_PLATFORM_VERSION=13
DEVICE_DEVICE_NAME=emulator-5554
DEVICE_UDID=emulator-5554

# Appium 配置
APPIUM_DRIVER_NAME=uiautomator2
APPIUM_DRIVER_VERSION=3.0.0
APPIUM_SERVER_HOST=127.0.0.1
APPIUM_SERVER_PORT=4723
```

## 快速开始

### 1. 运行测试

```bash
# 运行所有测试
python run_tests.py

# 运行指定模块测试
pytest tests/module/test_home.py -v

# 运行指定场景测试
pytest tests/scenario/test_full_order.py -v
```

### 2. 查看报告

测试执行完成后，会自动生成 Allure 报告：

- **报告路径**：`reports/allure-report/index.html`
- **查看方式**：使用浏览器打开该文件，或运行 `allure serve reports/allure-results`

## 测试执行

### 命令行参数

- **--env**：指定测试环境（dev/test/prod）
- **--alluredir**：指定 Allure 结果目录
- **--reruns**：失败重试次数
- **--reruns-delay**：重试间隔（秒）

### 示例命令

```bash
# 指定测试环境
pytest tests/ --env=test

# 失败重试
pytest tests/ --reruns=2 --reruns-delay=3

# 生成报告
pytest tests/ --alluredir=./reports/allure-results
```

## 报告生成

### Allure 报告特性

- **测试结果概览**：显示测试通过率、执行时间等
- **详细测试步骤**：记录每个测试步骤的执行情况
- **截图附件**：失败用例自动截图
- **环境信息**：显示测试环境配置
- **趋势分析**：历史测试结果对比

### 生成报告命令

```bash
# 生成报告
allure generate ./reports/allure-results -o ./reports/allure-report --clean

# 查看报告
allure serve ./reports/allure-results
```

## 最佳实践

### 1. 页面类设计

- **继承 BasePage**：所有页面类继承 BasePage，获得通用方法
- **封装元素操作**：将页面操作封装为方法，提高可读性
- **使用 PageFactory**：通过 PageFactory 统一管理页面实例

### 2. 测试用例设计

- **使用参数化**：通过 `@pytest.mark.parametrize` 实现数据驱动
- **添加 Allure 标注**：使用 `@allure.feature`、`@allure.story` 等标注测试用例
- **合理使用 fixture**：通过 fixture 管理测试数据和前置条件

### 3. 数据管理

- **Excel 数据**：适合表格形式的测试数据
- **YAML 数据**：适合结构化的测试数据
- **环境变量**：适合配置信息和敏感数据

### 4. 异常处理

- **显式等待**：使用 `WebDriverWait` 等待元素出现
- **失败重试**：使用 `--reruns` 参数实现失败自动重试
- **自动截图**：测试失败时自动截图并添加到报告

## 常见问题

### 1. 驱动安装失败

**问题**：`appium driver install uiautomator2` 失败

**解决方案**：
- 检查网络连接
- 使用代理安装：`appium driver install uiautomator2 --proxy http://your-proxy:port`
- 手动下载驱动包并安装

### 2. 设备连接问题

**问题**：`adb devices` 无法识别设备

**解决方案**：
- 检查 USB 连接
- 开启设备调试模式
- 安装设备驱动

### 3. 元素定位失败

**问题**：测试执行时元素定位失败

**解决方案**：
- 检查元素定位表达式是否正确
- 增加等待时间
- 检查应用是否处于正确状态

### 4. 报告生成失败

**问题**：Allure 报告生成失败

**解决方案**：
- 检查 Allure 命令是否正确
- 检查测试结果目录是否存在
- 检查 Allure 版本是否兼容

## 项目维护

### 1. 代码规范

- 遵循 PEP 8 代码规范
- 使用类型注解
- 编写清晰的文档字符串

### 2. 版本管理

- 使用 Git 进行版本控制
- 定期提交代码
- 编写有意义的提交信息

### 3. 持续集成

- 配置 CI/CD 流程
- 自动运行测试
- 生成测试报告

## 联系方式

- **项目维护**：测试团队
- **技术支持**：qa@example.com
- **文档更新**：2026-03-09

---

**备注**：本框架适用于小米商城等 Android 应用的自动化测试，可根据实际项目需求进行调整和扩展。