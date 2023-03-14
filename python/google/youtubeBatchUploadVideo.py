import os
import google.auth
import google.auth.transport.requests
import google.oauth2.credentials
import googleapiclient.discovery
import googleapiclient.errors

# 设置客户端 ID 和密钥
CLIENT_SECRETS_FILE = "client_secret.json"

# 设置用于请求 OAuth 2.0 令牌的范围
SCOPES = ["https://www.googleapis.com/auth/youtube.force-ssl"]
API_SERVICE_NAME = "youtube"
API_VERSION = "v3"


def get_authenticated_service():
    """获取经过身份验证的 YouTube 服务对象"""

    # 加载客户端密钥
    credentials = None
    if os.path.exists("token.json"):
        credentials = google.oauth2.credentials.Credentials.from_authorized_user_file("token.json", SCOPES)

    if not credentials or not credentials.valid:
        if credentials and credentials.expired and credentials.refresh_token:
            credentials.refresh(google.auth.transport.requests.Request())
        else:
            flow = google.auth.OAuth2WebServerFlow.from_client_secrets_file(CLIENT_SECRETS_FILE, SCOPES)
            credentials = google.auth.credentials.Credentials.from_authorized_user_info(flow.step1().exchange_code_for_token(input("授权码："))))

        # 将令牌写入文件中
        with open("token.json", "w") as token:
            token.write(credentials.to_json())

    return googleapiclient.discovery.build(API_SERVICE_NAME, API_VERSION, credentials=credentials)


def upload_video(youtube, title, description, file):
    """上传视频"""

    # 创建视频资源
    body = {
        "snippet": {
            "title": title,
            "description": description,
        },
        "status": {
            "privacyStatus": "private"
        }
    }

    # 创建媒体文件资源
    media = googleapiclient.http.MediaFileUpload(file, chunksize=-1, resumable=True)

    # 构建上传请求
    request = youtube.videos().insert(
        part=",".join(body.keys()),
        body=body,
        media_body=media
    )

    # 执行上传请求
    response = None
    error = None
    while response is None:
        try:
            print(f"正在上传视频：{file}...")
            status, response = request.next_chunk()
            if status:
                print(f"上传进度：{int(status.progress() * 100)}%")
        except googleapiclient.errors.HttpError as e:
            print(f"上传视频错误：{e}")
            error = e
            break

    if error:
        print(f"上传视频失败：{error}")
    else:
        print(f"视频已上传：https://www.youtube.com/watch?v={response['id']}")

# 调用上传视频函数
youtube = get_authenticated_service()
title = "测试视频"
description = "这是一个测试视频"
files = ["video1.mp4", "video2.mp4"]

for file in files:
    upload_video(youtube, title, description, file)