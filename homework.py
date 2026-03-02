from appium import webdriver
from appium.options.android import UiAutomator2Options
import time
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput

# 配置小米平板和作业帮应用信息
options = UiAutomator2Options()

# 平台类型（固定为Android）
options.platform_name = "Android"

# 设备名：可以使用任意名称或设备序列号
options.device_name = "24ecd0a2"
options.app_package = "com.baidu.homework"

# 作业帮应用的启动页
#options.app_activity = "com.baidu.homeworkhd.activity.index.HDIndexActivity"

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
   # print(f"🎯 启动页: {options.app_activity}")

    # 连接Appium Server（默认端口4723）
    driver = webdriver.Remote(
        command_executor="http://127.0.0.1:4723",
        options=options
    )

    driver.activate_app(options.app_package)

    el5 = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR,
                              value="new UiSelector().resourceId(\"com.baidu.homework:id/icon\").instance(0)")
    el5.click()
    el6 = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR,
                              value="new UiSelector().resourceId(\"com.baidu.homework:id/zyb\").instance(4)")
    el6.click()

    print(f"✅ 成功启动作业帮应用！")

    # 停留15秒，方便查看效果
    print("⏳ 应用已启动，将停留15秒...")
    # time.sleep(5)

    # 关闭应用连接
    driver.quit()
    print("✅ 已关闭应用连接")

except Exception as e:
  print(f"❌ 启动作业帮应用失败: {e}")
