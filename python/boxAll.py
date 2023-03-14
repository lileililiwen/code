#各种对话框窗体的实现
import tkinter.messagebox as messagebox

# 弹出消息对话框
messagebox.showinfo("提示", "这是一条提示信息")

import tkinter.simpledialog as simpledialog

# 弹出自定义输入对话框
result = simpledialog.askstring("输入", "请输入您的姓名：")
print("您输入的姓名是：", result)


import tkinter.filedialog as filedialog

# 弹出文件选择框
filename = filedialog.askopenfilename(title="选择文件", filetypes=(("文本文件", "*.txt"), ("所有文件", "*.*")))
print("您选择的文件是：", filename)


import tkinter.filedialog as filedialog

# 弹出文件夹选择框
dirname = filedialog.askdirectory(title="选择文件夹")
print("您选择的文件夹是：", dirname)