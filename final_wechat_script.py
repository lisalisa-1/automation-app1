from appium import webdriver
from appium.options.android import UiAutomator2Options
import time
import subprocess
import sys

# 获取设备序列号
def get_device_serial():
    try:
        result = subprocess.run(
            ['adb', 'devices'],
            capture_output=True,
            text=True,
            check=True
        )
        lines = result.stdout.strip().split('\n')
        for line in lines[1:]:
            if line.strip() and 'device' in line:
                return line.split('\t')[0]
    except Exception as e:
        print(f"获取设备序列号失败: {e}")
    return None

# 获取当前运行的Appium进程
def check_appium_running():
    try:
        result = subprocess.run(
            ['tasklist', '/FI', 'IMAGENAME eq node.exe'],
            capture_output=True,
            text=True
        )
        return 'node.exe' in result.stdout
    except Exception as e:
        print(f"检查Appium运行状态失败: {e}")
        return False

# 主程序
def main():
    # 检查Appium是否运行
    if not check_appium_running():
        print("❌ Appium Server未运行，请先启动Appium Server")
        print("启动命令: appium")
        sys.exit(1)
    else:
        print("✅ Appium Server已在运行")
    
    # 获取设备序列号
    device_serial = get_device_serial()
    if not device_serial:
        print("❌ 未检测到连接的设备，请确保设备已通过USB连接并启用USB调试")
        sys.exit(1)
    else:
        print(f"✅ 检测到设备: {device_serial}")
    
    # 检查微信是否已安装
    try:
        result = subprocess.run(
            ['adb', '-s', device_serial, 'shell', 'pm', 'list', 'packages', 'com.tencent.mm'],
            capture_output=True,
            text=True
        )
        if 'com.tencent.mm' not in result.stdout:
            print("❌ 设备上未安装微信应用")
            sys.exit(1)
        else:
            print("✅ 设备上已安装微信应用")
    except Exception as e:
        print(f"检查微信安装状态失败: {e}")
        sys.exit(1)
    
    # 配置Appium选项
    options = UiAutomator2Options()
    options.platform_name = "Android"
    options.device_name = device_serial
    options.app_package = "com.tencent.mm"
    options.app_activity = "com.tencent.mm.ui.LauncherUI"
    options.no_reset = True
    options.auto_grant_permissions = True
    options.new_command_timeout = 30
    options.udid = device_serial
    
    try:
        print("\n🚀 正在连接Appium Server...")
        print(f"📱 设备: {device_serial}")
        print(f"📦 应用: {options.app_package}")
        print(f"🎯 启动页: {options.app_activity}")
        
        # 连接Appium Server
        driver = webdriver.Remote(
            command_executor="http://127.0.0.1:4723",
            options=options
        )
        
        print("✅ Appium连接成功！")
        print("✅ 正在启动微信应用...")
        
        # 等待应用完全启动
        time.sleep(8)
        
        # 检查当前运行的应用
        current_package = driver.current_package
        print(f"📋 当前前台应用: {current_package}")
        
        if current_package == options.app_package:
            print("🎉 微信应用已成功启动并显示在前台！")
            print("⏳ 应用将保持运行15秒...")
            time.sleep(15)
        else:
            print(f"⚠️  前台应用不是微信: {current_package}")
            print("💡 尝试直接激活微信...")
            driver.activate_app(options.app_package)
            time.sleep(5)
            
            current_package = driver.current_package
            if current_package == options.app_package:
                print("🎉 微信应用已成功激活并显示在前台！")
                print("⏳ 应用将保持运行15秒...")
                time.sleep(15)
            else:
                print(f"❌ 无法激活微信应用，当前前台应用: {current_package}")
        
        # 关闭连接
        driver.quit()
        print("✅ 已关闭Appium连接")
        
    except Exception as e:
        print(f"\n❌ 错误类型: {type(e).__name__}")
        print(f"❌ 错误信息: {e}")
        import traceback
        traceback.print_exc()
        print("\n🔍 建议:")
        print("1. 检查Appium Server是否正常运行")
        print("2. 确保设备已授权USB调试")
        print("3. 尝试重启设备后再试")
        print("4. 确保Appium UIAutomator2驱动已安装")

if __name__ == "__main__":
    main()