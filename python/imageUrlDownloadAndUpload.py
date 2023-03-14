import os
import requests
import time
import pyautogui

# 定义图片下载函数
def download_image(url, dir_path):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            file_name = os.path.basename(url)
            file_path = os.path.join(dir_path, file_name)
            with open(file_path, 'wb') as f:
                f.write(response.content)
            return file_path
        else:
            return None
    except:
        return None

# 下载图片到指定目录
url = 'https://www.example.com/image.jpg'
dir_path = 'D:/images'
file_path = download_image(url, dir_path)

# 选择上传文件
if file_path:
    time.sleep(2)  # 等待文件下载完成
    pyautogui.click(500, 500)  # 点击上传按钮
    time.sleep(2)  # 等待上传对话框弹出
    pyautogui.write(file_path)  # 输入文件路径
    pyautogui.press('enter')  # 确认上传