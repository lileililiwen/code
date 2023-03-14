import time
import threading
import itchat
from pynput import keyboard

# 指定输入框的内容
input_text = ""

# 监听键盘事件
def on_press(key):
    try:
        # 判断是否按下回车键
        if key == keyboard.Key.enter:
            # 获取微信自己的用户名
            my_username = itchat.search_friends(name="雷阿伦")['UserName']
            print("myuserName"+my_username)

            # # 发送消息给自己
            # itchat.send(input_text, toUserName=my_username)
    except AttributeError:
        pass

def on_release(key):
    if key == keyboard.Key.esc:
        return False

# 启动键盘监听器
def start_listener():
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

# 启动微信登录
def login_wechat():
    itchat.auto_login(hotReload=True, enableCmdQR=2)
    itchat.run()

# 启动监听器和微信登录
def start():
    t1 = threading.Thread(target=start_listener)
    t2 = threading.Thread(target=login_wechat)
    t1.start()
    time.sleep(2)
    t2.start()

if __name__ == '__main__':
    # 启动监听器和微信登录
    start()
    # 指定输入框的内容，可以在监听键盘事件的回调函数中进行修改
    input_text = "Hello, world!"