#####################################带登录的简单图书管理系统，只是用来演示#################################################################################
import tkinter as tk
import mysql.connector as mysql
# # 连接MySQL数据库
# db = mysql.connect(
#     host="localhost",
#     user="remoteuser",
#     passwd="remotepassword",
#     database="library"
# )

import sqlite3
# 连接SQLite3数据库
db = sqlite3.connect("library.db")

# 创建图书表
cur = db.cursor()

# 登录函数
def login():
    # 检查用户名和密码
    if username_entry.get() == "admin" and password_entry.get() == "password":
        # 登录成功，关闭登录窗口
        login_window.destroy()
        # 打开主窗口
        open_main_window()
    else:
        # 登录失败，弹出提示框
        tk.messagebox.showwarning(title="登录失败", message="用户名或密码不正确！")
# 创建主窗口
def open_main_window():
    window = tk.Tk()
    window.title("图书管理系统")

    # 创建标签和输入框
    tk.Label(window, text="书名").grid(row=0)
    title_entry = tk.Entry(window)
    title_entry.grid(row=0, column=1)

    tk.Label(window, text="作者").grid(row=1)
    author_entry = tk.Entry(window)
    author_entry.grid(row=1, column=1)

    # 创建列表框
    book_listbox = tk.Listbox(window, width=50)
    book_listbox.grid(row=2, column=0, columnspan=2)
    # 创建滚动条
    scrollbar = tk.Scrollbar(window)
    scrollbar.grid(row=2, column=2, rowspan=6)

    # 将滚动条和列表框关联起来
    book_listbox.configure(yscrollcommand=scrollbar.set)
    scrollbar.configure(command=book_listbox.yview)

    # 为列表框添加数据
    cur.execute("SELECT * FROM book")
    rows = cur.fetchall()
    for row in rows:
        book_listbox.insert(tk.END, row)


    # 创建按钮
    search_button = tk.Button(window, text="查询", command=search_books)
    search_button.grid(row=3, column=0)

    borrow_button = tk.Button(window, text="借阅", command=borrow_book)
    borrow_button.grid(row=3, column=1)

    return_button = tk.Button(window, text="归还", command=return_book)
    return_button.grid(row=3, column=2)
    # 运行窗口
    window.mainloop()


    # 查询图书
    def search_books():
        book_listbox.delete(0, tk.END)
        cur.execute("SELECT * FROM book WHERE title LIKE %s OR author LIKE %s", (f"%{title_entry.get()}%", f"%{author_entry.get()}%"))
        books = cur.fetchall()
        for book in books:
            book_listbox.insert(tk.END, f"{book[0]} - {book[1]} by {book[2]} ({'available' if book[3] else 'not available'})")

    # 借阅图书
    def borrow_book():
        selected_book = book_listbox.get(tk.ACTIVE)
        book_id = int(selected_book.split('-')[0].strip())
        cur.execute("UPDATE book SET available = 0 WHERE id = %s", (book_id,))
        db.commit()
        search_books()

    # 归还图书
    def return_book():
        selected_book = book_listbox.get(tk.ACTIVE)
        book_id = int(selected_book.split('-')[0].strip())
        cur.execute("UPDATE book SET available = 1 WHERE id = %s", (book_id,))
        db.commit()
        search_books()


# 执行主程序
if __name__ == '__main__':
    cur.execute("CREATE TABLE IF NOT EXISTS book (id INT AUTO_INCREMENT PRIMARY KEY, title VARCHAR(255), author VARCHAR(255), available BOOLEAN)")

    # 初始化 10 条数据
    cur.execute("INSERT INTO book (title, author, available) VALUES (?, ?, ?)",("Python编程入门", "张三",True));
    cur.execute("INSERT INTO book (title, author, available) VALUES (?, ?, ?)",("Python编程进阶", "李四", True));
    # 提交更改
    db.commit();

    # 创建登录窗口
    login_window = tk.Tk()
    login_window.title("登录")

    # 创建标签和输入框
    tk.Label(login_window, text="用户名").grid(row=0)
    username_entry = tk.Entry(login_window)
    username_entry.grid(row=0, column=1)

    tk.Label(login_window, text="密码").grid(row=1)
    password_entry = tk.Entry(login_window, show="*")
    password_entry.grid(row=1, column=1)

    # 创建登录按钮
    login_button = tk.Button(login_window, text="登录", command=login)
    login_button.grid(row=2, column=0, columnspan=2)

    # 运行窗口
    login_window.mainloop()