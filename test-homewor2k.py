from appium import webdriver
from appium.options.android import UiAutomator2Options  # 3.x 导入路径不变，但驱动需手动装
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.appiumby import AppiumBy
import time

# ===================== 第一步：配置 Android 设备和作业帮 APP =====================
options = UiAutomator2Options()
# 1. 设备序列号（adb devices 查看，必填）
#options.udid = "1234567890ABCDEF"  # 替换成你的设备ID，如 emulator-5554（模拟器）
# 2. 作业帮固定配置（无需修改）
options.app_package = "com.baidu.homework"  # 作业帮包名
#options.app_activity = ".activity.SplashActivity"  # 作业帮启动页
# 3. 通用优化配置
options.no_reset = True  # 不重置APP数据，避免每次重装
options.unicode_keyboard = True  # 支持中文输入
options.reset_keyboard = True  # 操作后还原键盘
options.new_command_timeout = 30  # 超时时间（3.x 推荐显式设置）

# ===================== 第二步：初始化驱动并执行点击操作 =====================
try:
    # 连接 Appium Server（3.x 地址不变，驱动需提前安装）
    driver = webdriver.Remote(
        command_executor="http://127.0.0.1:4723",
        options=options
    )
    driver.implicitly_wait(10)  # 全局隐式等待
    print("✅ 成功启动作业帮 APP（Appium 3.x）")

    # 等待启动页/广告加载（作业帮启动有广告，3.x 建议延长等待）
    time.sleep(6)

    # ===================== 核心：点击作业帮「搜题」按钮 =====================
    # 方式1：XPath 定位（文本“搜题”，通用且无需依赖 Inspector）
    search_btn = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((AppiumBy.XPATH, "//*[@text='搜题']"))
    )
    # 方式2：ID 定位（更稳定，需从 Appium Inspector 获取实际 ID，示例：
    # search_btn = WebDriverWait(driver, 20).until(
    #     EC.element_to_be_clickable((AppiumBy.ID, "com.baidu.homework:id/iv_search"))
    # )

    search_btn.click()
    print("✅ 成功点击「搜题」按钮")

    # 验证跳转（可选）
    time.sleep(3)
    print("✅ 已跳转到搜题页面，操作完成")

except Exception as e:
    print(f"❌ 操作失败：{str(e)}")
    # 3.x 新增：可选保存错误截图（方便排查）
    if 'driver' in locals():
        driver.save_screenshot("error_3x.png")
        print("❌ 错误截图已保存为 error_3x.png")
finally:
    # 调试时可注释 driver.quit()，保留界面查看结果
    if 'driver' in locals():
        driver.quit()
    print("📌 脚本执行结束")