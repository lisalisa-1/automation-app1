from selenium import webdriver
from appium.options.common import AppiumOptions  # Appium 3.X 正确的导入路径

# 1. 初始化 AppiumOptions 对象
options = AppiumOptions()

# 2. 设置核心配置（以安卓为例，iOS 只需调整对应 capability）
# 设备/系统相关
options.set_capability('platformName', 'Android')
options.set_capability('platformVersion', '13')  # 你的设备系统版本
options.set_capability('deviceName', 'Android Emulator')  # 设备名称/模拟器名称
#options.set_capability('udid', 'Android Emulator')  # 设备名称/模拟器名称

# App 相关
options.set_capability('appPackage', 'com.xiaomi.shop')  # 被测 App 包名
options.set_capability('appActivity', 'com.xiaomi.shop2.activity.MainActivity')  # 被测 App 启动页
options.set_capability('automationName', 'UiAutomator2')  # 自动化引擎（安卓用 UiAutomator2，iOS 用 XCUITest）

# 可选配置（提升稳定性）
options.set_capability('noReset', True)  # 不重置 App 数据
options.set_capability('newCommandTimeout', 30)  # 命令超时时间

# 3. 初始化 Remote 驱动（核心步骤）
# Appium 服务默认地址：http://127.0.0.1:4723/wd/hub（Appium 3.X 仍兼容此路径）
driver = webdriver.Remote(
    command_executor='http://127.0.0.1:4726',
    options=options  # 3.X 直接传 options 对象，不再需要 desired_capabilities 参数
)

# 4. 简单操作示例（验证驱动可用）
print(f"当前设备分辨率：{driver.get_window_size()}")

# 5. 关闭驱动（必须执行，释放资源）
driver.quit()