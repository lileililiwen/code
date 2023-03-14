from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# 账号密码
username = "your_username"
password = "your_password"

# 打开浏览器并进入百度文库登录页面
# driver = webdriver.Chrome()

#https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/
# # 设置Edge WebDriver路径
edge_driver_path = 'c:\\msedgedriver.exe'

# 创建Edge浏览器对象
edge_options = webdriver.EdgeOptions()
edge_options.use_chromium = True
edge_options.add_argument('disable-gpu')
driver = webdriver.Edge(executable_path=edge_driver_path, options=edge_options)
driver.get("https://passport.baidu.com/v2/?login")

# 登录
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "tang-pass-footerBarULogin")))  # 等待登录按钮出现
driver.find_element_by_class("tang-pass-footerBarULogin").click()  # 点击登录按钮
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "TANGRAM__PSP_4__userName")))  # 等待用户名输入框出现
driver.find_element_by_id("TANGRAM__PSP_4__userName").send_keys(username)  # 输入用户名
driver.find_element_by_id("TANGRAM__PSP_4__password").send_keys(password)  # 输入密码
driver.find_element_by_id("TANGRAM__PSP_4__submit").click()  # 点击登录按钮

# 等待登录完成
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "task_success")))  # 等待任务完成按钮出现

# 遍历文件列表并上传
filenames = ["file1.docx", "file2.docx", "file3.docx"]
for filename in filenames:
    # 进入上传页面
    driver.get("https://wenku.baidu.com/user/interfaceupload")

    # 上传文件
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "uploadFile")))  # 等待文件上传按钮出现
    driver.find_element_by_id("uploadFile").send_keys(filename)  # 上传文件
    time.sleep(5)  # 等待上传完成

    # 点击上传按钮
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "uploadButton")))  # 等待上传按钮出现
    driver.find_element_by_id("uploadButton").click()

    # 等待上传完成
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//div[@class="msg-upload-success"]')))  # 等待上传成功提示出现

print("全部上传完成！")

# 关闭浏览器
driver.quit()