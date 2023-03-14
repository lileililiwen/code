import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

# 初始化
root = tk.Tk()
root.title('My App')
root.geometry('400x300')
root.resizable(False, False)

# Label标签
label = tk.Label(root, text='Hello World!', font=('Arial', 18))
label.pack()

# Button按钮
def on_click():
    messagebox.showinfo('Message', 'You clicked the button!')

button = tk.Button(root, text='Click Me', command=on_click)
button.pack()

# Entry输入框
entry = tk.Entry(root, width=20)
entry.pack()

# Text文本框
text = tk.Text(root, height=5)
text.pack()

# Checkbutton复选框
chk_var = tk.BooleanVar()
chk = tk.Checkbutton(root, text='Check Me', variable=chk_var)
chk.pack()

# Radiobutton单选框
radio_var = tk.StringVar()
radio1 = tk.Radiobutton(root, text='Option 1', value='1', variable=radio_var)
radio1.pack()
radio2 = tk.Radiobutton(root, text='Option 2', value='2', variable=radio_var)
radio2.pack()

# Listbox列表框
listbox = tk.Listbox(root)
listbox.pack()
for item in ['apple', 'banana', 'orange']:
    listbox.insert(tk.END, item)

# Combobox下拉框
combo_var = tk.StringVar()
combo = ttk.Combobox(root, textvariable=combo_var, values=['apple', 'banana', 'orange'])
combo.pack()

# Spinbox计数器
spinbox = tk.Spinbox(root, from_=0, to=10)
spinbox.pack()

# Scale滑块
scale = tk.Scale(root, from_=0, to=100, orient=tk.HORIZONTAL)
scale.pack()

# Menu菜单
menubar = tk.Menu(root)
menu_file = tk.Menu(menubar, tearoff=0)
menu_file.add_command(label='New')
menu_file.add_command(label='Open')
menu_file.add_separator()
menu_file.add_command(label='Exit', command=root.quit)
menubar.add_cascade(label='File', menu=menu_file)
root.config(menu=menubar)

# 运行主循环
root.mainloop()