from instabot import Bot

bot = Bot()
bot.login(username='your_username', password='your_password')

# 从文本文件中获取图片和描述
import os
folder_path = '/path/to/folder'
description_file_path = '/path/to/description_file.txt'

with open(description_file_path, 'r') as f:
    descriptions = f.readlines()

descriptions = [d.strip() for d in descriptions if d.strip()] # 去除空行和空格
image_paths = [os.path.join(folder_path, f) for f in os.listdir(folder_path) if f.endswith('.jpg')]

# 发布图片
for i, image_path in enumerate(image_paths):
    description = descriptions[i % len(descriptions)] # 循环使用描述
    bot.upload_photo(image_path, caption=description)

bot.logout()

# 这个代码首先通过 open 函数打开一个文本文件，从中读取所有行并保存到 descriptions 变量中。然后，它获取文件夹中所有 .jpg 后缀的图片路径，并将每张图片的描述设置为 descriptions 列表中的相应元素。在上传图片时，它循环使用 descriptions 列表中的描述，直到所有图片都被上传。
# 你可以将 'your_username'、'your_password'、'/path/to/folder' 和 '/path/to/description_file.txt' 替换为相应的值。注意，文本文件中的描述应该和图片文件名的数量一致，否则会出现错误。