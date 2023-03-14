import requests

# Bilibili API 授权认证，获取 access_token
def get_access_token():
    url = "https://passport.bilibili.com/oauth2/token"
    data = {
        "grant_type": "client_credentials",
        "client_id": "YOUR_APP_KEY",
        "client_secret": "YOUR_APP_SECRET"
    }
    response = requests.post(url, data=data)
    return response.json()['access_token']

import requests

# Bilibili API 创建上传任务，获取 upload_id 和 upload_url
def create_upload_task(access_token,fileData):
    url = "https://member.bilibili.com/x/vu/web/create?csrf=YOUR_CSRF_TOKEN"
    headers = {
        "Authorization": f"Bearer {access_token}",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }
    ##TODO 这里写死的，还没有利用fileData
    data = {
        "filename": "test.mp4",
        "filesize": 1024,
        "title": "Test Video",
        "tid": 17,
        "desc": "This is a test video.",
        "source": "原创",
        "cover": "http://i2.hdslb.com/bfs/archive/44148b8d169f187c7fbdec62c96f2a7d8356b3a7.jpg",
        "tag": "Test, Video",
        "open_elec": 0,
        "open_screen": 0,
        "no_reprint": 0,
        "interactive": 0,
        "is_steins_gate": 0
    }
    response = requests.post(url, headers=headers, data=data)
    response_json = response.json()
    return response_json['data']['upload_id'], response_json['data']['upload_url']

# 使用 upload/url 接口进行文件上传
def upload_video(access_token, upload_id, upload_url):
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "multipart/form-data"
    }
    files = {'video': open('test.mp4', 'rb')}
    data = {'chunk': 0, 'chunks': 1, 'upload_id': upload_id}
    response = requests.post(upload_url, headers=headers, data=data, files=files)
    return response.json()    

import os

# Bilibili API 相关信息
access_key = 'your_access_key'
secret_key = 'your_secret_key'
access_token=get_access_token()
space_id = 1234567  # 你的账号的空间 ID
# 上传视频文件夹路径
video_folder_path = '/path/to/your/video/folder'

# 获取视频文件夹中所有视频文件路径
video_file_paths = [os.path.join(video_folder_path, filename) for filename in os.listdir(video_folder_path) if filename.endswith('.mp4')]

# 遍历视频文件路径列表，逐个上传视频
for video_file_path in video_file_paths:
    # 上传视频
    result = create_upload_task(access_token,{
        "video_file_path":video_file_path,
        "space_id":space_id,
        "title":'My video title',
        "desc":'My video description',
        "tag":'tag1,tag2,tag3',
        "cover":None,  # 不使用封面图片
        "source":None,  # 不使用来源链接
        "no_reprint":False,  # 允许转载
        "open_elec":False,  # 不开启选电视
        "max_retry":5,  # 最大重试次数
        "retry_delay":5,  # 重试间隔秒数
        "verify_ssl":True,  # 启用 SSL 验证
        "timeout":None  # 默认超时时间
    })
    
    # 输出上传结果
    print(result)

    #*result是由来解元组
    upload_resp = upload_video(access_token,*result)

    print(upload_resp)

def getCSRfToken():
    # 创建Session对象
    session = requests.Session()

    # 登录B站，获取Cookie
    login_url = 'https://passport.bilibili.com/login'
    params = {
        'username': 'your_username',
        'password': 'your_password',
        'captcha': '',
        'csrf': ''
    }
    session.post(login_url, data=params)
    # 访问B站首页，获取CSRF Token
    index_url = 'https://www.bilibili.com/'
    response = session.get(index_url)
    csrf_token = response.cookies.get('bili_jct')
    return csrf_token