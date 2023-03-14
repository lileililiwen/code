import tweepy

# 填写您的 API key 和 API secret key
consumer_key = "YOUR_CONSUMER_KEY"
consumer_secret = "YOUR_CONSUMER_SECRET"

# 填写您的 access token 和 access token secret
access_token = "YOUR_ACCESS_TOKEN"
access_token_secret = "YOUR_ACCESS_TOKEN_SECRET"

# 登录到 Twitter API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# 图片文件名列表和推文列表
image_files = ['image1.jpg', 'image2.jpg', 'image3.jpg']
tweets = ["Tweet 1 with image1", "Tweet 2 with image2", "Tweet 3 with image3"]

# 上传图片并发布带图片的推文
for i in range(len(image_files)):
    # 上传图片
    media = api.media_upload(image_files[i])

    # 发布推文
    api.update_status(status=tweets[i], media_ids=[media.media_id])

# 在上面的代码中，您需要将 YOUR_CONSUMER_KEY，YOUR_CONSUMER_SECRET，YOUR_ACCESS_TOKEN 和 YOUR_ACCESS_TOKEN_SECRET 替换为您的 Twitter 开发者帐户中的 API 密钥和访问令牌。然后，将 image_files 列表替换为您要上传的图片文件名列表，将 tweets 列表替换为您要发布的推文列表。

# 运行上面的脚本后，它将登录到您的 Twitter 帐户并发布带有图片的推文，每个推文都包含一个上传的图片。    