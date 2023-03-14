from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 设置Appium Server的地址和端口

# /wd/hub：这是Appium Server提供的Webdriver端点，通过该端点可以进行手机操作、应用测试等，使用的是HTTP协议，默认端口号为4723。
# /status：该端点用于获取Appium Server的状态信息，使用的是HTTP协议，默认端口号为4723。
# /sessions：该端点用于获取当前会话列表，使用的是HTTP协议，默认端口号为4723。
# /appium/device：该端点用于获取设备信息，使用的是HTTP协议，默认端口号为4723。
# /appium/settings：该端点用于获取和修改Appium Server的设置信息，使用的是HTTP协议，默认端口号为4723。
# 在启动Appium Server时，可以通过命令行参数或配置文件等方式指定Appium Server的端口号。一般情况下，Appium Server默认使用的端口号为4723。因此，在Python中调用Appium服务时，需要指定该端点地址为http://localhost:4723/wd/hub。如果Appium Server使用的端口号不是默认的4723端口，需要将该端口号与localhost替换成实际的服务器地址和端口号。

appium_server_url = "http://localhost:4723/wd/hub"

# 定义测试设备的相关配置
desired_caps = {}
desired_caps['platformName'] = 'Android' # 指定操作系统为Android
desired_caps['platformVersion'] = '12' # 指定操作系统版本
desired_caps['deviceName'] = '21ba4d99' # 指定设备名称


# 通常情况下，可以通过以下几种方式来查找应用的包名和启动Activity：

# 通过应用商店查找：在应用商店中搜索待测应用，进入应用详情页面，包名和Activity名称通常会显示在页面底部或开发者信息中。

# 通过AndroidManifest.xml查找：在Android应用的源代码中，可以找到AndroidManifest.xml文件，其中包含了应用的基本信息，包名和Activity名称也会在其中声明。

# 通过命令行查找：使用ADB命令连接手机或模拟器，在命令行中输入adb shell dumpsys window windows | grep -E 'mCurrentFocus'可以查看当前应用的Activity名称。进一步通过adb shell pm list packages命令可以列出当前安装的应用的包名。

# 一旦确定了应用的包名和启动Activity名称，就可以在测试脚本中指定appPackage和appActivity参数，以便Appium正确地启动应用并执行测试。

desired_caps['appPackage'] = 'com.android.calculator2' # 指定要测试的应用包名
desired_caps['appActivity'] = 'com.android.calculator2.Calculator' # 指定要测试的应用启动Activity

# 启动Appium会话
driver = webdriver.Remote(appium_server_url, desired_caps)

# 查找并点击按钮
button_7 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'com.android.calculator2:id/digit_7')))
button_7.click()

# 查找并点击按钮
button_add = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'com.android.calculator2:id/op_add')))
button_add.click()

# 查找并点击按钮
button_3 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'com.android.calculator2:id/digit_3')))
button_3.click()

# 查找并点击按钮
button_equal = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'com.android.calculator2:id/eq')))
button_equal.click()

# 查找结果并打印
result = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'com.android.calculator2:id/result')))
print(result.text)

# 结束Appium会话
driver.quit()