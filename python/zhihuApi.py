import requests
import json

# 获取token
client_id = "your_client_id"
client_secret = "your_client_secret"
username = "your_username"
password = "your_password"
url = "https://www.zhihu.com/api/v3/oauth/sign_in"

headers = {
    "Referer": "https://www.zhihu.com/signup",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
}

data = {
    "client_id": client_id,
    "client_secret": client_secret,
    "username": username,
    "password": password
}

session = requests.Session()
response = session.post(url, headers=headers, data=data)
r = json.loads(response.text)
access_token = r["access_token"]

# 调用API
url = "https://www.zhihu.com/api/v3/topics"
headers = {
    "Referer": "https://www.zhihu.com/topics",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
    "Authorization": "Bearer " + access_token
}

response = session.get(url, headers=headers)
print(response.text)