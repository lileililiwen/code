import requests
from io import BytesIO
from PIL import Image, ImageDraw, ImageFont
import jieba.analyse
from google_images_search import GoogleImagesSearch
import paddleseg

# 配置 Google Images Search API
gis = GoogleImagesSearch('your_project_cx', 'your_api_key')
gis.session.verify = False

# 提取标题关键词
title = "这是一篇关于Python的文章"
keywords = jieba.analyse.extract_tags(title, topK=5)

# 搜索匹配图片
gis.search({'q': ' '.join(keywords), 'num': 10})
results = gis.results()

# 处理图片背景
for i, result in enumerate(results):
    # 下载图片
    response = requests.get(result.url)
    img = Image.open(BytesIO(response.content))
    # 提取背景
    # 这里使用了 PaddleSeg 这个深度学习库来进行图像分割，需要自行安装
    # 可以使用其他图像分割库来替代
    bg_mask = paddleseg.predict('/path/to/model', img)
    bg = Image.fromarray(bg_mask.astype('uint8') * 255)
    # 替换背景
    bg = bg.resize(img.size)
    img.putalpha(bg)
    # 保存图片
    img.save(f'image_{i}.png')

# 填充文字
text = "这是一篇关于Python的文章"
font = ImageFont.truetype('/path/to/font.ttf', 36)

for i, result in enumerate(results):
    # 打开图片
    img = Image.open(f'image_{i}.png').convert('RGBA')
    # 创建绘图对象
    draw = ImageDraw.Draw(img)
    # 计算文本位置
    text_size = draw.textsize(text, font)
    x = (img.width - text_size[0]) / 2
    y = (img.height - text_size[1]) / 2
    # 填充文本
    draw.text((x, y), text, fill=(255, 255, 255), font=font)
    # 保存图片
    img.save(f'image_{i}.png')