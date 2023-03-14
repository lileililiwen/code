import requests
import time
import datetime
from toutiao import TouTiao, TouTiaoError
app_id = 'your-app-id'
app_secret = 'your-app-secret'


import requests

# 设置请求的 URL 和参数
url = 'https://developer.toutiao.com/api/apps/token'
params = {
    'appid': app_id,
    'secret': app_secret,
    'grant_type': 'client_credential'
}

# 发送请求并获取响应
response = requests.get(url, params=params)
result = response.json()

# 提取 access_token 并输出
if 'access_token' in result:
    access_token = result['access_token']
    print(f"access_token: {access_token}")
else:
    print("获取 access_token 失败")



#access_token = 'your-access-token'

toutiao = TouTiao(app_id=app_id, app_secret=app_secret, access_token=access_token)

response = toutiao.micro_app.create(title='微头条标题', content='微头条内容', image_file='image.png', image_type='file')


video_url = 'your-video-url'
response = toutiao.video.upload(video_url, title='视频标题', desc='视频描述')


now = datetime.datetime.now()
scheduled_publish_time = int(time.mktime(now.timetuple()) + 3600)  # 设置为一小时后发布

image_file = 'image.png'
with open(image_file, 'rb') as f:
    image_data = f.read()

params = {
    'title': '文章标题',
    'content': '文章内容',
    'cover_image': ('image.png', image_data),
    'publish_time': scheduled_publish_time
}

response = toutiao.article.create(params)
