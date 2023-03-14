import requests
import json

# 填写您的 APP Key 和 APP Secret
app_key = "YOUR_APP_KEY"
app_secret = "YOUR_APP_SECRET"

# 填写您的 access token 和 access token secret
access_token = "YOUR_ACCESS_TOKEN"
access_token_secret = "YOUR_ACCESS_TOKEN_SECRET"

# 获取 access_token
url = "https://api.weibo.com/oauth2/access_token"
data = {
    "grant_type": "client_credentials",
    "client_id": app_key,
    "client_secret": app_secret
}
response = requests.post(url, data=data)
access_token = json.loads(response.text)['access_token']

# 微博文本列表和图片文件名列表
text_list = ["My first weibo with image1", "My second weibo with image2", "My third weibo with image3"]
image_files = ['image1.jpg', 'image2.jpg', 'image3.jpg']

# 上传图片并发布微博
for i in range(len(text_list)):
    # 上传图片
    url = "https://api.weibo.com/2/statuses/upload_url_text.json"
    files = {'pic': open(image_files[i], 'rb')}
    response = requests.post(url, files=files, data={"access_token": access_token})
    pic_url = json.loads(response.text)['pic_url']

    # 发布微博
    url = "https://api.weibo.com/2/statuses/update.json"
    data = {
        "access_token": access_token,
        "status": text_list[i] + " " + pic_url
    }
    response = requests.post(url, data=data)

# 在上面的代码中，您需要将 YOUR_APP_KEY 和 YOUR_APP_SECRET 替换为您在新浪微博开发者中心注册的应用程序的 APP Key 和 APP Secret。然后，将 text_list 列表替换为您要发布的微博文本列表，将 image_files 列表替换为您要上传的图片文件名列表。

# 运行上面的脚本后，它将登录到您的新浪微博帐户并发布带有图片的微博，每个微博都包含一个上传到微博图片服务器的图片。