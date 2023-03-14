import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import tkinter as tk


# 登录网站并返回登录后的 token
def login_website(username, password):
    # 初始化浏览器
    browser = webdriver.Chrome()
    browser.get("https://example.com/login")

    # 输入用户名和密码
    username_input = browser.find_element_by_id("username")
    username_input.send_keys(username)
    password_input = browser.find_element_by_id("password")
    password_input.send_keys(password)

    # 点击登录按钮
    login_button = browser.find_element_by_id("login-button")
    login_button.click()

    # 等待页面加载完成
    browser.implicitly_wait(10)

    # 解析页面获取 token
    soup = BeautifulSoup(browser.page_source, "html.parser")
    token = soup.find("meta", {"name": "csrf-token"})["content"]

    # 关闭浏览器
    browser.quit()

    return token


# 提交表单到其他网站
def submit_form_to_other_website(token, data):
    headers = {"X-CSRF-Token": token}
    url = "https://other-website.com/submit/form"
    response = requests.post(url, data=data, headers=headers)
    if response.status_code == 200:
        print("提交成功！")
    else:
        print("提交失败：{}".format(response.status_code))


# 显示表单填写界面
def show_form_window():
    print("hhhhhhhhhhhhhhhh")
    window = tk.Tk()
    window.title("表单填写")

    # 标题输入框
    title_label = tk.Label(window, text="标题")
    title_label.pack()
    title_entry = tk.Entry(window)
    title_entry.pack()

    # 内容输入框
    content_label = tk.Label(window, text="内容")
    content_label.pack()
    content_entry = tk.Entry(window)
    content_entry.pack()

    # 图片上传按钮
    image_button = tk.Button(window, text="上传图片")
    image_button.pack()

    # 提交按钮
    submit_button = tk.Button(window, text="提交", command=lambda: submit_form(title_entry.get(), content_entry.get()))
    submit_button.pack()

    window.mainloop()


# 提交表单
def submit_form(title, content):
    # 登录第一个网站并获取 token
    username = "your-username"
    password = "your-password"
    token = login_website(username, password)

    # 提交表单到其他网站
    data = {"title": title, "content": content}
    submit_form_to_other_website(token, data)


if __name__ == '__main__':
    # 显示表单填写界面
    show_form_window()