from appium import webdriver
from appium.options.android import UiAutomator2Options
import time

# 获取设备序列号
def get_device_serial():
    import subprocess
    try:
        result = subprocess.run(
            ['adb', 'devices'],
            capture_output=True,
            text=True,
            check=True
        )
        lines = result.stdout.strip().split('\n')
        for line in lines[1:]:  # 跳过第一行 "List of devices attached"
            if line.strip() and 'device' in line:
                return line.split('\t')[0]
    except Exception as e:
        print(f"获取设备序列号失败: {e}")
    return None

# 获取设备序列号
device_serial = get_device_serial()
print(f"检测到设备序列号: {device_serial}")

# 配置小米平板和微信应用信息
options = UiAutomator2Options()

# 平台类型（固定为Android）
options.platform_name = "Android"

# 设备名：使用实际设备序列号
if device_serial:
    options.device_name = device_serial
else:
    options.device_name = "XiaomiTablet"

# 微信应用的包名
options.app_package = "com.tencent.mm"

# 微信应用的启动页
options.app_activity = "com.tencent.mm.ui.LauncherUI"

# 不重置应用数据（避免每次打开都清除缓存）
options.no_reset = True

# 自动授权应用权限
options.auto_grant_permissions = True

# 设置新命令等待超时时间
options.new_command_timeout = 60

# 如果有多个设备，指定UDID
if device_serial:
    options.udid = device_serial

try:
    print("🚀 正在启动Appium连接...")
    print(f"📱 设备序列号: {device_serial}")
    print(f"📦 应用包名: {options.app_package}")
    print(f"🎯 启动页面: {options.app_activity}")
    
    # 连接Appium Server
    driver = webdriver.Remote(
        command_executor="http://127.0.0.1:4723",
        options=options
    )
    
    print(f"✅ Appium连接成功！")
    print(f"✅ 正在启动微信应用...")
    
    # 等待应用完全启动
    time.sleep(5)
    
    # 检查应用是否在前台运行
    current_package = driver.current_package
    current_activity = driver.current_activity
    
    print(f"📋 当前前台应用: {current_package}")
    print(f"📋 当前前台页面: {current_activity}")
    
    if current_package == options.app_package:
        print("✅ 微信应用已成功启动并在前台运行！")
    else:
        print(f"⚠️  前台应用不是微信，而是: {current_package}")
        print("💡 尝试直接启动微信...")
        driver.activate_app(options.app_package)
        time.sleep(3)
        current_package = driver.current_package
        if current_package == options.app_package:
            print("✅ 微信应用已成功启动并在前台运行！")
        else:
            print(f"❌ 无法将微信应用切换到前台，当前前台应用: {current_package}")
    
    # 停留15秒，方便查看效果
    print("⏳ 应用已启动，将停留15秒...")
    time.sleep(15)
    
except Exception as e:
    print(f"❌ 错误: {type(e).__name__}: {e}")
    import traceback
    traceback.print_exc()
    print("\n🔍 故障排查建议:")
    print("1. 确保Appium Server已启动（命令: appium）")
    print("2. 确保设备已通过USB连接并启用USB调试")
    print("3. 检查设备是否已授权ADB调试")
    print("4. 确保微信应用已安装在设备上")
    print("5. 尝试手动通过adb启动微信验证: adb shell am start -n com.tencent.mm/com.tencent.mm.ui.LauncherUI")
    
finally:
    if 'driver' in locals():
        # 关闭应用连接
        driver.quit()
        print("✅ 已关闭Appium连接")