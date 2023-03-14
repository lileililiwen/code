from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# 使用 token 登录网站
def login_website(token):
    # 初始化浏览器
    browser = webdriver.Chrome()
    browser.get("https://example.com/login")

    #https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/
    # # 设置Edge WebDriver路径
    # edge_driver_path = '/path/to/msedgedriver'

    # # 创建Edge浏览器对象
    # edge_options = webdriver.EdgeOptions()
    # edge_options.use_chromium = True
    # edge_options.add_argument('disable-gpu')
    # edge_browser = webdriver.Edge(executable_path=edge_driver_path, options=edge_options)

    # # 访问网页
    # edge_browser.get('https://www.example.com')

    # 添加 token 到请求头
    headers = {"X-CSRF-Token": token}
    browser.execute_script("window.localStorage.setItem('auth_token', '{}')".format(token))
    browser.refresh()

    # 等待页面加载完成
    WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID, "nav")))

    return browser


# 根据 CSS 选择器点击元素
def click_by_css_selector(browser, css_selector):
    element = browser.find_element_by_css_selector(css_selector)
    element.click()


# 根据 XPATH 选择器点击元素
def click_by_xpath_selector(browser, xpath_selector):
    element = browser.find_element_by_xpath(xpath_selector)
    element.click()


# 根据 CSS 选择器填写输入框
def fill_input_by_css_selector(browser, css_selector, value):
    element = browser.find_element_by_css_selector(css_selector)
    element.clear()
    element.send_keys(value)


# 根据 XPATH 选择器填写输入框
def fill_input_by_xpath_selector(browser, xpath_selector, value):
    element = browser.find_element_by_xpath(xpath_selector)
    element.clear()
    element.send_keys(value)


# 根据 CSS 选择器勾选单选框
def check_radio_by_css_selector(browser, css_selector):
    element = browser.find_element_by_css_selector(css_selector)
    element.click()


# 根据 XPATH 选择器勾选单选框
def check_radio_by_xpath_selector(browser, xpath_selector):
    element = browser.find_element_by_xpath(xpath_selector)
    element.click()


# 根据 CSS 选择器勾选复选框
def check_checkbox_by_css_selector(browser, css_selector):
    element = browser.find_element_by_css_selector(css_selector)
    if not element.is_selected():
        element.click()


# 根据 XPATH 选择器勾选复选框
def check_checkbox_by_xpath_selector(browser, xpath_selector):
    element = browser.find_element_by_xpath(xpath_selector)
    if not element.is_selected():
        element.click()


if __name__ == '__main__':
    # 使用 token 登录网站
    token = "your-token"
    browser = login_website(token)

    # 点击按钮
    click_by_css_selector(browser, "#button-id")
    click_by_xpath_selector(browser, "//button[contains(text(), 'Button Text')]")

    # 填写输入框
    fill_input_by_css_selector(browser, "#input-id", "Input Value")
    fill_input_by_xpath_selector(browser, "//input[@id='input-id']", "Input Value")

    # 勾选单选框
    check_radio_by_css_selector(browser, "#radio-id")
    check_radio_by_xpath_selector(browser, "//input[@id='radio-id']")

    # 勾选复选框
    check_checkbox_by_css_selector(browser, "#checkbox-id")
    check_checkbox_by_xpath_selector(browser, "//input[@id='checkbox-id']")

    # 关闭浏览器
    browser.quit()
