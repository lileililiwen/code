import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import  QWidget
from PyQt5.QtWidgets import  QLabel
from PyQt5.QtWidgets import  QLineEdit
from PyQt5.QtWidgets import  QTextEdit
from PyQt5.QtWidgets import  QPushButton
from PyQt5.QtWidgets import  QGridLayout
from PyQt5.QtWidgets import  QDesktopWidget
from PyQt5.QtGui import QPixmap,QIcon
 

class Form(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 设置窗口标题
        self.setWindowTitle('表单')

        # 设置窗口大小和位置
        self.resize(500, 600)
        self.center()

        # 设置窗口图标
        self.setWindowIcon(QIcon('icon.png'))

        # 标题
        lbl_title = QLabel('标题:')
        self.edit_title = QLineEdit()

        # 内容
        lbl_content = QLabel('内容:')
        self.edit_content = QTextEdit()

        # 图片地址1
        lbl_img1 = QLabel('图片地址1:')
        self.edit_img1 = QLineEdit()

        # 图片地址2
        lbl_img2 = QLabel('图片地址2:')
        self.edit_img2 = QLineEdit()

        # 图片地址3
        lbl_img3 = QLabel('图片地址3:')
        self.edit_img3 = QLineEdit()

        # 提交按钮
        btn_submit = QPushButton('提交')
        btn_submit.clicked.connect(self.submit)

        # 清空按钮
        btn_clear = QPushButton('清空')
        btn_clear.clicked.connect(self.clear)

        # 创建网格布局
        grid = QGridLayout()

        # 添加控件到网格布局
        grid.addWidget(lbl_title, 1, 0)
        grid.addWidget(self.edit_title, 1, 1)
        grid.addWidget(lbl_content, 2, 0)
        grid.addWidget(self.edit_content, 2, 1)
        grid.addWidget(lbl_img1, 3, 0)
        grid.addWidget(self.edit_img1, 3, 1)
        grid.addWidget(lbl_img2, 4, 0)
        grid.addWidget(self.edit_img2, 4, 1)
        grid.addWidget(lbl_img3, 5, 0)
        grid.addWidget(self.edit_img3, 5, 1)
        grid.addWidget(btn_submit, 6, 0)
        grid.addWidget(btn_clear, 6, 1)
        grid.addWidget(QLabel())

        # 设置窗口布局为网格布局
        self.setLayout(grid)

    def center(self):
        # 获取窗口框架的几何形状
        qr = self.frameGeometry()

        # 获取屏幕的中心位置
        cp = QDesktopWidget().availableGeometry().center()

        # 设置窗口框架的中心位置为屏幕中心位置
        qr.moveCenter(cp)

        # 将窗口左上角的位置设置为窗口框架的左上角位置，从而实现窗口居中
        self.move(qr.topLeft())


    def inputForm(self,data):
     
        # 创建浏览器实例
        driver = webdriver.Chrome()
        # 打开指定网页
        url = "https://mp.toutiao.com/profile_v4/weitoutiao/publish"
        driver.get(url)

        # 填写表单
        form = driver.find_element_by_name("form_name")
        input1 = form.find_element_by_name("input1_name")
        input1.send_keys("input1_value")
        input2 = form.find_element_by_name("input2_name")
        input2.send_keys("input2_value")
        input3 = form.find_element_by_name("input3_name")
        input3.send_keys("input3_value")

        # 点击指定按钮
        button = form.find_element_by_name("button_name")
        button.click()        

    def submit(self):
        # 获取输入框中的内容
        title = self.edit_title.text()
        content = self.edit_content.toPlainText()
        img1 = self.edit_img1.text()
        img2 = self.edit_img2.text()

        # 在这里可以将内容提交到后台进行处理，这里只是简单地打印内容
        print('标题:', title)
        print('内容:', content)
        print('图片地址1:', img1)
        print('图片地址2:', img2)
        print('图片地址3:', img2)
        data={"title":title,"content":content}
        self.inputForm(data)
        self.clear()

    def clear(self):
        # 清空所有输入框
        self.edit_title.clear()
        self.edit_content.clear()
        self.edit_img1.clear()
        self.edit_img2.clear()
        self.edit_img3.clear()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = Form()
    form.show()
    sys.exit(app.exec_())


