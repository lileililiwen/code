from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
import time

# 配置连接真实的Android手机的参数
desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '10'
desired_caps['deviceName'] = 'Android'
desired_caps['udid'] = 'XXXXXXXXXXXX'  # 填入手机的设备ID
desired_caps['appPackage'] = 'com.android.settings'
desired_caps['appActivity'] = '.Settings'
desired_caps['adbExecTimeout'] = 20000  # 设置ADB命令执行超时时间

# 连接手机
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

# 找到要点击的元素并点击
el = driver.find_element_by_xpath("//android.widget.TextView[@text='WLAN']")
action = TouchAction(driver)
action.tap(el).perform()

# 等待1秒钟
time.sleep(1)

# 关闭连接
driver.quit()