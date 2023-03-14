###试验结果是失败的，地址或者哪里有问题
import requests
import json

# 设置请求头
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
    'Referer': 'https://mp.toutiao.com/profile_v4/publication.html',
    'Origin': 'https://mp.toutiao.com',
    'X-Requested-With': 'XMLHttpRequest',
    'Accept-Encoding': 'gzip, deflate, br',
    'Content-Type': 'application/json',
    'Cookie': 'gfgarrcache_103ffe65=1; passport_csrf_token=d8a5fe0c5f7924c7f820f2085df63f1f; passport_csrf_token_default=d8a5fe0c5f7924c7f820f2085df63f1f; _ba=BA0.2-20230212-5110e-jCYQEPdkwH05dNCEKECD; s_v_web_id=verify_le0t252e_YkUUL7bv_VX2A_4ScX_AHWp_aJ0I6dfBR86q; csrf_session_id=2a52f61bdb0fa604c8218c2ceea7fe83; ttcid=66be0a491abb4ea6bb9963bfef317ae522; _ga=GA1.1.1057183030.1678263790; _S_WIN_WH=1872_936; _S_DPR=1; _S_IPAD=0; gftoken=YWQ3MjFmNDUzMnwxNjc4MzI0MzgwNzR8fDAGBgYGBgY; _tea_utm_cache_1231={%22utm_source%22:%22magic%22}; xigua_csrf_token=Ow7DKG-8U0Cur9WKLXT0dxyh; xg_p_tos_token=61fb20073bfc2cc35a5dcafa1c6abdcd; msToken=6YOugjDrvz3zmcIWbSbgocTIDKlvcwfqa48ebbRx3CMX5AF98EYKPlhK0-GptnNN6yECI0LSSUz52YyqF6qZTd-pa6Tx9j5zzHY1_LpW7OMjYsZFL9RwdQ==; msToken=0MXD6QGJlP2CEJJ2E0fAIr9fpcmvpmk2k2m23YH3-8H3Dkl5bG07uZfT6Ech0nxA8EE1Ap--G8ApJ-Dp_f8SufDsA-7nemS0FDYr5T2zTf5kum3sbFLL8Q==; tt_scid=MrxAeHnc.5ieQ-EXkoN4bvzkZdI0KhODK78b.KWX5uc2iHuujNVNYILkZoo1uibG7086; _ga_QEHZPBE5HH=GS1.1.1678609903.7.1.1678611653.0.0.0'  # 在此处填入你的cookie
}

# 设置上传图片的URL和参数
img_upload_url = 'https://mp.toutiao.com/tools/upload_picture/?type=ueditor&pgc_watermark=1&action=uploadimage&encode=utf-8&inajax=1&bkt=toutu.oss-hz.qbox.me&token=0f33d6b1622d9b51f9b1aeb1275c5d5e5b6c5b6f902cf6d5f55c5e6cb9ac00df&file=images%2F'
img_params = {
    'filename': ('filename', open('img.jpg', 'rb'), 'image/jpeg')
}

# 定义上传图片函数
def upload_img():
    img_resp = requests.post(img_upload_url, files=img_params, headers=headers)
    if img_resp.status_code == 200:
        img_json = json.loads(img_resp.text)
        img_url = img_json['data']['url']
        img_width = img_json['data']['width']
        img_height = img_json['data']['height']
        return {'url': img_url, 'width': img_width, 'height': img_height}
    else:
        return None

# 定义发布微头条函数
def post_micro_article(content, img_urls):
    # 上传图片，获取图片URL
    img_list = []
    for img_url in img_urls:
        img_params['filename'] = ('filename', open(img_url, 'rb'), 'image/jpeg')
        print(img_params)
        img_info = upload_img()
        if img_info:
            img_list.append({'url': img_info['url'], 'width': img_info['width'], 'height': img_info['height']})

    # 设置请求参数
    post_data = {
        'content': content,
        'image_list': img_list,
        'activity_ids': [],
        'video_id': '',
        'origin_group_id': '',
        'question_id': '',
        'answer_id': '',
        'promote_status': 0,
        'auto_analysis': 0,
        'template_id': ''
    }

    # 发送POST请求
    post_url = 'https://mp.toutiao.com/core/article/new_article_v2/?source=mp&type=mp'
    post_resp = requests.post(post_url, data=json.dumps(post_data), headers=headers)
    print("post_resp"+str(post_resp.status_code))
    if post_resp.status_code == 200:
        print('发布成功！')
    else:
        print('发布失败！')

if __name__ == '__main__':
    # 调用发布微头条函数
    content = '这是一条微头条！'
    img_urls = ['1.jpg', '1.jpeg', '1.png']
    post_micro_article(content, img_urls)