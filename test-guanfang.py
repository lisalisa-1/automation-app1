import unittest
from time import sleep

from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver import WebElement
from appium.webdriver.common.appiumby import AppiumBy


capabilities = dict(
    platformName='Android',
    automationName='uiautomator2',
    deviceName='emulator-5554',
    appPackage='com.android.settings',
    appActivity='com.android.settings.Settings',
    language='en',
    locale='US'
)

appium_server_url = 'http://localhost:4723'

class TestAppium(unittest.TestCase):
    def setUp(self) -> None:
        print("1")
        self.driver = webdriver.Remote(appium_server_url, options=UiAutomator2Options().load_capabilities(capabilities))

    def tearDown(self) -> None:
        if self.driver:
           self.driver.quit()
           print("0")

    def test_find_battery(self) -> None:
        from time import sleep
        # el2 = self.driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR,
        #                           value="new UiSelector().resourceId(\"android:id/icon\").instance(0)")
        # el22 = self.driver.find_element(by=AppiumBy.XPATH,
        # value = '(//android.widget.ImageView[@resource-id="android:id/icon"])[1]')
        #
        # el22.click()
        #
        #
        #
        # el3 = self.driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR,
        #                           value="new UiSelector().resourceId(\"android:id/summary\").instance(0)")
        # el3.click()
        el1 = self.driver.find_element(by=AppiumBy.ID, value="com.android.settings:id/search_action_bar_title")
        el1.click()
        el2 = self.driver.find_element(by=AppiumBy.ID, value="android:id/search_src_text")
        el2.send_keys("battery")
        el3=self.driver.find_elements(by=AppiumBy.XPATH,
        value="(//android.widget.TextView[@resource-id='android:id/title'])")
        print("搜索结果数量:", len(el3))
        for item in el3:
            print(item.text)
    def test_find_saerch(self) -> None:
        #sleep(2)
        el1 = self.driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR,
                                   value="new UiSelector().resourceId(\"android:id/icon\").instance(0)")
        el1.click()
        sleep(5)
        switchElement=self.driver.find_element(by=AppiumBy.XPATH,
        value="//android.widget.Switch[@content-desc=\"Wi‑Fi\"]")
        print("Wi-Fi开关状态:", switchElement.is_selected())
        if not switchElement.is_selected():
            switchElement.click()  #




if __name__ == '__main__':
    unittest.main()