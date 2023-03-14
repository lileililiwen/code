import os
import sys
import time
import subprocess
import pyperclip
import pyautogui

# 剪贴板操作

# 复制文本到剪贴板
pyperclip.copy('Hello, world!')

# 从剪贴板中读取文本
text = pyperclip.paste()
print(text)

# 开关机操作

# 关机
os.system('shutdown -s')

# 重启
os.system('shutdown -r')

# 屏幕操作

# 输入文字
pyautogui.typewrite('Hello, world!')

# 清除屏幕
if sys.platform == 'win32':
    subprocess.call('cls', shell=True)
else:
    subprocess.call('clear', shell=True)