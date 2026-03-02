from appium import webdriver
import time

# 配置连接参数
desired_caps = {
    'platformName': 'Android',           # 设备平台
    'platformVersion': '13',             # 平板电脑的 Android 版本号 (请根据实际情况修改)
    'deviceName': '24ecd0a2',    # 平板电脑的设备名称 (通过 adb devices 命令查看)
    'appPackage': 'com.tencent.mm',      # 微信应用包名
    'appActivity': '.ui.LauncherUI',     # 微信启动 Activity
    'noReset': True,                     # 不重置应用状态，避免重新登录
    'unicodeKeyboard': True,             # 使用 Unicode 键盘
    'resetKeyboard': True                # 测试后重置键盘
}

# Appium 服务器地址
server_url = 'http://127.0.0.1:4723/wd/hub'

# 启动会话
driver = webdriver.Remote(server_url, options=desired_caps)

# 等待微信应用启动
time.sleep(5)

print("微信应用已成功打开！")

# 此处可以添加后续操作，例如点击搜索按钮等
# driver.find_element_by_accessibility_id("搜索").click()

# 保持脚本运行，方便观察
input("按回车键退出...")
driver.quit()
