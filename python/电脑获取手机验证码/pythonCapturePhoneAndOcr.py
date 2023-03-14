# pip install androidviewclient
#连接手机并且截图并且识别验证码
from com.dtmilano.android.viewclient import ViewClient
import time

# 连接手机
device, serialno = ViewClient.connectToDeviceOrExit()


# # 启动应用程序
# package_name = 'com.example.myapp'
# activity_name = '.MainActivity'
# device.startActivity(component=(package_name, activity_name))

# # 等待应用程序启动
# vc = ViewClient(device, serialno)
# vc.dump()

# main_activity = vc.findViewById('android:id/content')
# main_activity.wait()

# # 点击按钮
# button = vc.findViewById('com.example.myapp:id/my_button')
# button.touch()


# # 获取文本元素
# text_view = vc.findViewById('com.example.myapp:id/my_text_view')
# text = text_view.getText()
# print('文本元素内容：', text)


# 截图并保存到本地
screenshot = device.takeSnapshot()
with open('screenshot.png', 'wb') as f:
    screenshot.save(f, 'PNG')

# 识别验证码
from PIL import Image
import pytesseract

# 读取截图文件
img = Image.open('screenshot.png')

# 裁剪出验证码区域
#x1, y1, x2, y2
# 除了 Android Studio 的布局分析工具之外，还有一些第三方工具可以用来查看 Android 应用程序的 UI 层次结构和属性。

# 以下是一些常用的工具：

# UI Automator Viewer：这是 Android SDK 自带的一个 UI 工具，可以帮助您查看 Android 应用程序的 UI 层次结构和属性。在命令行中输入 uiautomatorviewer 即可打开该工具。该工具支持通过 Android 设备或模拟器连接到应用程序，并可查看应用程序中所有的 UI 元素及其属性。

# Appium Desktop：这是一款开源的自动化测试工具，可以用来测试 Android 应用程序和其他平台的应用程序。Appium Desktop 可以通过 UI Automator 和其他工具来获取应用程序的 UI 层次结构和属性。您可以使用该工具查看应用程序中的所有 UI 元素，包括布局 ID。

# Selendroid：这是一款基于 Selenium 的自动化测试工具，可以用来测试 Android 应用程序。Selendroid 可以通过 UI Automator 和其他工具来获取应用程序的 UI 层次结构和属性。您可以使用该工具查看应用程序中的所有 UI 元素，包括布局 ID。

# 请注意，这些工具可能需要一些技术知识和配置才能正常运行。如果您不熟悉这些工具或遇到问题，请参考它们的官方文档或寻求帮助。
crop_region = (400,420,646,700) # 根据实际情况设置裁剪区域

try:
    crop_img = img.crop(crop_region)
except ValueError:
    print('裁剪区域超出了原始图像的范围')
    crop_img = None

if crop_img:
    # 识别验证码
    print("crop_img")
    # 将图像转换为灰度图像
    # .convert() 方法可以接受不同的参数，用于将图像转换为不同的模式。

    # 以下是 .convert() 可接受的一些常用参数：

    # 'L': 将图像转换为灰度图像，每个像素只有一个亮度值。
    # '1': 将图像转换为二值图像，每个像素只有0和1两个值。
    # 'RGB': 将图像转换为红、绿和蓝（RGB）模式，每个像素由三个值表示。
    # 'RGBA': 将图像转换为带有透明度（Alpha）通道的 RGBA 模式，每个像素由四个值表示。
    # 除了上述常用参数之外，.convert() 方法还支持其他一些参数，例如 'CMYK'、'HSV'、'LAB' 等，用于将图像转换为不同的颜色模式或颜色空间。
    image = crop_img.convert('L')
    code = pytesseract.image_to_string(crop_img)
    print('最新验证码：', code)