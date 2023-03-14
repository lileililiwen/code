from pywinauto import application
from pywinauto import timings
from pywinauto.findwindows import ElementNotFoundError

app = application.Application()
# 打开目标窗口
app.start('notepad.exe')

# 等待窗口出现
notepad_window = timings.WaitUntilPasses(20, 0.5, lambda: app.window(title='无标题 - 记事本'))

# 拖动窗体
notepad_window.MoveWindow(100, 100, 400, 400)

# 找到元素并点击
try:
    notepad_window.Edit.TypeKeys("Hello, World!")
    notepad_window.MenuSelect("文件->保存")
    save_window = timings.WaitUntilPasses(20, 0.5, lambda: app.window(title='另存为'))
    save_window['Edit'].TypeKeys('test.txt')
    save_window['Button'].Click()
except ElementNotFoundError:
    print("找不到元素")

# 读取内容
notepad_window.Edit.SetEditText("")
notepad_window.MenuSelect("编辑->粘贴")
assert notepad_window.Edit.GetLine(0) == "Hello, World!"

# 关闭窗口
notepad_window.Close()
notepad_window.WaitNot('exists')