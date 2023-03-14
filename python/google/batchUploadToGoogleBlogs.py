import httplib2
import os
import sys
import datetime
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google.oauth2.credentials import Credentials
from google.oauth2 import service_account

# 谷歌博客的ID
BLOG_ID = '<YOUR_BLOG_ID>'

# JSON文件路径和API范围
JSON_FILE_PATH = '<PATH_TO_JSON_FILE>'
SCOPES = ['https://www.googleapis.com/auth/blogger']

# 创建凭据对象
credentials = service_account.Credentials.from_service_account_file(JSON_FILE_PATH, scopes=SCOPES)

# 创建Blogger API客户端
blogger = build('blogger', 'v3', credentials=credentials)

# 上传图片并获取链接
def upload_image(file_path):
    try:
        # 获取上传图片的URL
        upload_url = blogger.media().upload(blogId=BLOG_ID, media_body=file_path).execute()['url']
        # 将URL转换为HTML标签，以便将图片插入博客内容
        img_html = f'<img src="{upload_url}">'
        return img_html
    except HttpError as error:
        print(f'An error occurred: {error}')
        return None

# 创建上传博客的函数
# 要获取谷歌博客的ID，请按照以下步骤操作：

# 登录到谷歌博客的管理界面。

# 选择您要使用的博客。

# 点击左侧菜单栏中的“设置”。

# 点击“基本信息”选项卡。

# 在“博客ID”字段下，您将看到一个长字符串。这就是您的谷歌博客ID。

# 请注意，如果您有多个博客，则需要对每个博客重复上述步骤以获取其相应的ID。
def create_blog_post(title, content, image_file_path):
    # 如果提供了图片文件路径，则上传图片并将其添加到博客内容中
    if image_file_path:
        img_html = upload_image(image_file_path)
        if img_html:
            content += img_html

    body = {
        'kind': 'blogger#post',
        'title': title,
        'content': content,
        'labels': ['python', 'api'],
        'published': datetime.datetime.utcnow().isoformat() + 'Z',
    }

    posts = blogger.posts()
    posts.insert(blogId=BLOG_ID, body=body).execute()

# 批量上传博客
titles = ['Title 1', 'Title 2', 'Title 3']
contents = ['Content 1', 'Content 2', 'Content 3']
image_file_paths = ['<PATH_TO_IMAGE_FILE_1>', '<PATH_TO_IMAGE_FILE_2>', '<PATH_TO_IMAGE_FILE_3>']

for i in range(len(titles)):
    create_blog_post(titles[i], contents[i], image_file_paths[i])