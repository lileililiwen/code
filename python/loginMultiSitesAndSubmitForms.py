from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# 创建一个 Chrome 浏览器实例
driver = webdriver.Chrome()

# 打开网站1，并登录
driver.get('https://example.com/site1')
username = driver.find_element_by_name('username')
password = driver.find_element_by_name('password')
login_button = driver.find_element_by_name('login')
username.send_keys('my_username')
password.send_keys('my_password')
login_button.click()

# 打开网站2，并登录
driver.execute_script('window.open("https://example.com/site2");')
driver.switch_to.window(driver.window_handles[1])
username = driver.find_element_by_name('username')
password = driver.find_element_by_name('password')
login_button = driver.find_element_by_name('login')
username.send_keys('my_username')
password.send_keys('my_password')
login_button.click()

# 填写表单
driver.execute_script('window.open("https://example.com/form");')
driver.switch_to.window(driver.window_handles[2])
name = driver.find_element_by_name('name')
email = driver.find_element_by_name('email')
submit_button = driver.find_element_by_name('submit')
name.send_keys('my_name')
email.send_keys('my_email')
submit_button.click()

# 等待 5 秒钟，然后关闭浏览器
time.sleep(5)
driver.quit()