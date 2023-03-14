import pytesseract
from PIL import Image, ImageFilter

# 读取图片
image = Image.open('image.jpg')

# 将图片转换为灰度图像
gray_image = image.convert('L')

# 对灰度图像应用二值化阈值
threshold_image = gray_image.point(lambda x: 0 if x < 100 else 255)

# 应用图像增强
enhanced_image = threshold_image.filter(ImageFilter.EDGE_ENHANCE)

# 识别文本
text = pytesseract.image_to_string(enhanced_image, lang='eng')

# 打印文本
print(text)



# 读取票据或身份证
image = Image.open('receipt.jpg')

# 将图片转换为灰度图像
gray_image = image.convert('L')

# 对灰度图像应用二值化阈值
threshold_image = gray_image.point(lambda x: 0 if x < 100 else 255)

# 应用图像增强
enhanced_image = threshold_image.filter(ImageFilter.EDGE_ENHANCE)

# 识别文本
text = pytesseract.image_to_string(enhanced_image, lang='chi_sim')

# 打印文本
print(text)