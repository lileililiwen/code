import requests
import json

# 1. 设置请求参数
app_id = '你的AppID'
app_secret = '你的AppSecret'
access_token_url = 'https://api.weixin.qq.com/cgi-bin/token'
access_token_params = {
    'grant_type': 'client_credential',
    'appid': app_id,
    'secret': app_secret
}

# 2. 获取 access_token
access_token_resp = requests.get(access_token_url, params=access_token_params)
access_token_resp_dict = json.loads(access_token_resp.text)
access_token = access_token_resp_dict['access_token']

# 3. 获取聊天记录
msg_url = 'https://api.weixin.qq.com/cgi-bin/xxx/xxx'  # 请替换为实际的接口地址
msg_params = {
    'access_token': access_token,
    'xxx': 'xxx'  # 请替换为实际的请求参数
}

msg_resp = requests.get(msg_url, params=msg_params)
msg_resp_dict = json.loads(msg_resp.text)

# 4. 根据关键词搜索聊天内容
keyword = '关键词'
for msg in msg_resp_dict['msgs']:
    content = msg.get('content', '')
    if keyword in content:
        print(content)