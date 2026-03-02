from appium import webdriver
from appium.options.android import UiAutomator2Options
import time

# 配置小米平板和目标应用信息
options = UiAutomator2Options()
# 平台类型（固定为Android）
options.platform_name = "Android"
# 设备名：可任意填写（adb devices 里的序列号也可以）
options.device_name = "24ecd0a2"
# 关键：替换为目标应用的包名
options.app_package = "com.tencent.mm"
# 关键：替换为目标应用的启动页
options.app_activity = "com.tencent.mm.ui.LauncherUI"
# 不重置应用数据（避免每次打开都清缓存）
options.no_reset = True
# 自动授权应用权限（小米平板适配）
options.auto_grant_permissions = True

try:
    # 连接Appium Server（默认端口4723）
    driver = webdriver.Remote(
        command_executor="http://127.0.0.1:4723/wd/hub",
        options=options
    )
    print(f"✅ 成功打开应用：{options.app_package}")
    # 停留10秒，方便查看效果
    time.sleep(10)
except Exception as e:
    print(f"❌ 打开应用失败：{str(e)[:200]}")
    print("\n🔍 排查方向：")
    print("1. 包名/启动页是否填写正确？")
    print("2. 平板是否已通过adb连接电脑？")
    print("3. Appium Server是否已启动？")
finally:
    # 关闭应用连接
    if 'driver' in locals():
        driver.quit()
        print("✅ 已关闭应用连接")