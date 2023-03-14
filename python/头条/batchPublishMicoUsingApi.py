import requests
import json

# 上传图片并返回图片ID
def upload_image(file_path, access_token):
    url = 'https://mp.toutiao.com/tools/upload_picture/?type=ueditor&pgc_watermark=1&action=uploadimage&encode=utf-8'
    headers = {
        'Authorization': 'Bearer ' + access_token,
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
    }
    files = {'file': ('image.jpg', open(file_path, 'rb'), 'image/jpeg')}
    response = requests.post(url, headers=headers, files=files)
    result = json.loads(response.text)
    if result['success']:
        return result['data']['pic_info']['pic_id']
    else:
        return None

# 发布微头条
def publish_micro_article(access_token, content, image_ids, publish_time=None):
    url = 'https://mp.toutiao.com/mp/agw/article/publish/'
    headers = {
        'Authorization': 'Bearer ' + access_token,
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
    }
    data = {
        'content': content,
        'image_infos': [{'pic_id': id} for id in image_ids],
    }
    if publish_time:
        data['publish_time'] = publish_time
    response = requests.post(url, headers=headers, json=data)
    result = json.loads(response.text)
    if result['success']:
        return result['data']['article_id']
    else:
        return None

# 使用示例
if __name__ == '__main__':
    app_id="";
    app_secret="";
    # 填写access_token、要发布的内容和图片路径列表
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

    
    #access_token = 'your_access_token'
    content = '这是一条带多张图片的微头条'
    image_paths = ['image1.jpg', 'image2.jpg', 'image3.jpg']
    image_ids = []
    for image_path in image_paths:
        id = upload_image(image_path, access_token)
        if id:
            image_ids.append(id)
    article_id = publish_micro_article(access_token, content, image_ids)
    if article_id:
        print('微头条发布成功，文章ID为：', article_id)
    else:
        print('微头条发布失败')