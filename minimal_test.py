# 极简版Appium测试脚本
import sys
print("Python版本:", sys.version)

# 导入必要的模块
try:
    from appium import webdriver
    from appium.options.android import UiAutomator2Options
    print("✅ 成功导入Appium模块")
except ImportError as e:
    print(f"❌ 导入Appium模块失败: {e}")
    sys.exit(1)

# 配置最基本的选项
options = UiAutomator2Options()
options.platform_name = "Android"
options.device_name = "XiaomiTablet"
options.app_package = "com.tencent.mm"
options.app_activity = "com.tencent.mm.ui.LauncherUI"
options.no_reset = True

# 尝试连接Appium Server
try:
    print("尝试连接Appium Server...")
    driver = webdriver.Remote(
        command_executor="http://127.0.0.1:4723",
        options=options
    )
    print("✅ 连接成功！")
    
    # 停留5秒
    import time
    time.sleep(5)
    
    # 关闭连接
    driver.quit()
    print("✅ 已关闭连接")
    
except Exception as e:
    print(f"❌ 错误: {type(e).__name__}: {e}")
    import traceback
    traceback.print_exc()