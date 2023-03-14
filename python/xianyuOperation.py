#闲鱼操作
import requests
import json


#获取token 
def getToken(app_key,app_secret):
    url = 'https://oauth.taobao.com/token'
    params = {
        'grant_type': 'client_credentials',
        'client_id': app_key,
        'client_secret': app_secret,
        'scope': 'tanx_app'
    }
    response = requests.post(url, params=params)
    data = response.json()

    if 'access_token' in data:
        token = data['access_token']
        print(f'Token: {token}')
    else:
        print(f'Error: {data}')




#查询商品列表：
def getGoodList(token):
    url = 'https://api.xianyu.ali.com/core/search'
    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json'
    }
    params = {
        'catId': '50100309',
        'from': 0,
        'sort': 'recent',
        'q': 'iphone'
    }
    response = requests.post(url, headers=headers, json=params)
    data = response.json()

    if 'items' in data:
        items = data['items']
        for item in items:
            print(f'{item["title"]} - {item["price"]}')
    else:
        print(f'Error: {data}')    



#发布商品：
def publishGood(token):
    url = 'https://api.xianyu.ali.com/core/post'
    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json'
    }
    params = {
        'content': {
            'title': 'iPhone XS Max',
            'desc': '全网通，正品保证',
            'categoryId': '50100309',
            'price': 9999,
            'postageFee': 0,
            'picUrls': ['https://www.example.com/1.jpg', 'https://www.example.com/2.jpg'],
            'location': {
                'province': '浙江省',
                'city': '杭州市',
                'district': '西湖区',
                'address': '西溪花园'
            }
        }
    }
    response = requests.post(url, headers=headers, json=params)
    data = response.json()

    if 'postId' in data:
        post_id = data['postId']
        print(f'Post ID: {post_id}')
    else:
        print(f'Error: {data}')


#刷新商品：
def refreshGood(token,post_id):
    url = f'https://api.xianyu.ali.com/core/refresh/{post_id}'
    headers = {
        'Authorization': f'Bearer {token}'
    }
    response = requests.post(url, headers=headers)
    data = response.json()

    if 'success' in data and data['success']:
        print(f'Refresh success')
    else:
        print(f'Error: {data}')

#编辑商品：
##TODO 这里截断了
def editGood(token,post_id):
    pass
    # url = f'https://api.xianyu.ali.com/core/post/{post_id}'
    # headers = {
    #     'Authorization': f'Bearer {token}',
    #     'Content-Type': 'application/json'
    # }
    # params = {
    #     'content': {
    #         'title': 'iPhone XS Max',
    #         'desc': '全网通，正品保证',
    #         'categoryId': '


#设置自动回复
def autoReply(app_key,item_id,content):
    ## 设置闲鱼 API 地址和 appKey
    url = 'https://api.zhetaoke.com:10001/api/open_ztk_service/xianyu_private_message_add.ashx'
    # 设置自动回复的商品 ID 和回复内容
    # 组织请求参数
    params = {
        'appkey': app_key,
        'itemid': item_id,
        'content': content
    }

    # 发送 POST 请求
    response = requests.post(url, data=params)

    # 打印响应结果
    print(response.text)    


#查询商品id和分类id
def findGoodAndCat(areadCode):
    # API地址
    url = 'http://api.xianyu.163.com/item/categories/get'
    # 请求参数
    params = {
        'pid': 0,  # 一级类目
        'areaCode': 440100,  # 广州地区编码
        'source': 1  # 接口来源（1为客户端）
    }

    # 发送HTTP GET请求
    response = requests.get(url, params=params)

    # 解析JSON数据
    json_data = json.loads(response.text)

    # 打印商品分类id和名称
    if json_data['success']:
        for category in json_data['data']:
            print('分类ID：', category['categoryId'], '分类名称：', category['categoryName'])


# 执行主程序
if __name__ == '__main__':
   app_key=""
   app_secret=""
   getToken(app_key,app_secret)
   