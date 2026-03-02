import traceback
import sys
from appium import webdriver
from appium.options.android import UiAutomator2Options

# 配置小米平板和目标应用信息
options = UiAutomator2Options()
options.platform_name = "Android"
options.device_name = "XiaomiTablet"
options.app_package = "com.tencent.mm"
options.app_activity = "com.tencent.mm.ui.LauncherUI"
options.no_reset = True
options.auto_grant_permissions = True

try:
    print("尝试连接到Appium Server...")
    print(f"URL: http://127.0.0.1:4723")
    print(f"Options: {options}")
    
    # 连接Appium Server
    driver = webdriver.Remote(
        command_executor="http://127.0.0.1:4723",
        options=options
    )
    
    print(f"✅ 成功打开应用：{options.app_package}")
    
    # 关闭连接
    driver.quit()
    print("✅ 已关闭应用连接")
    
except Exception as e:
    print(f"❌ 错误类型: {type(e).__name__}")
    print(f"❌ 错误信息: {e}")
    print("\n🔍 完整错误堆栈:")
    traceback.print_exc()
    sys.exit(1)