from appium import webdriver
from appium.options.android import UiAutomator2Options
import time

# 配置小米平板和微信应用信息
options = UiAutomator2Options()

# 平台类型（固定为Android）
options.platform_name = "Android"

# 设备名：可以使用任意名称或设备序列号
options.device_name = "24ecd0a2"

# 微信应用的包名
options.app_package = "com.tencent.mm"

# 微信应用的启动页
options.app_activity = "com.tencent.mm.ui.LauncherUI"

# 不重置应用数据（避免每次打开都清除缓存）
options.no_reset = True

# 自动授权应用权限
options.auto_grant_permissions = True

# 设置设备UDID（如果有多个设备连接时需要指定）
# options.udid = "设备序列号"

try:
    print("🚀 正在启动Appium连接...")
    print(f"📱 设备: {options.device_name}")
    print(f"📦 应用: {options.app_package}")
    print(f"🎯 启动页: {options.app_activity}")
    
    # 连接Appium Server（默认端口4723）
    driver = webdriver.Remote(
        command_executor="http://127.0.0.1:4723",
        options=options
    )

    driver.activate_app(options.app_package)

    
    print(f"✅ 成功启动微信应用！")
    
    # 停留15秒，方便查看效果
    print("⏳ 应用已启动，将停留15秒...")
    #time.sleep(5)
    
    # 关闭应用连接
    driver.quit()
    print("✅ 已关闭应用连接")
    
except Exception as e:
    print(f"❌ 启动微信应用失败: {e}")
    print("\n🔍 故障排查建议:")
    print("1. 确保Appium Server已启动（命令: appium）")
    print("2. 确保设备已通过USB连接并启用USB调试")
    print("3. 检查设备是否已授权ADB调试")
    print("4. 确保微信应用已安装在设备上")
    print("5. 检查Appium UIAutomator2驱动是否已安装")
    print("   (安装命令: appium driver install uiautomator2)")