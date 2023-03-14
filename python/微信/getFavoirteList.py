import requests
import json

# 应用的app id和app secret，需要在微信开放平台创建应用后获取
appid = "your appid"
appsecret = "your appsecret"

# 获取access token
url = "https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=" + appid + "&secret=" + appsecret
response = requests.get(url)
access_token = json.loads(response.text)["access_token"]

# 获取收藏夹列表
url = "https://api.weixin.qq.com/cgi-bin/favorites/getlist?access_token=" + access_token
response = requests.get(url)
favorites = json.loads(response.text)["item"]

# 输出收藏夹信息
for favorite in favorites:
    print("标题：", favorite["title"])
    print("链接：", favorite["link"])
    print("描述：", favorite["desc"])
    print("时间：", favorite["ctime"])
    print("图片：", favorite["thumburl"])
    print("---------------------------")