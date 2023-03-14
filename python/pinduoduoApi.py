import requests
import hashlib
import json

# API请求地址
api_url = 'https://open.yangkeduo.com/api/router'

# 拼多多开放平台提供的app_key和app_secret
app_key = 'your_app_key'
app_secret = 'your_app_secret'

def getGoodDetail(app_key):
    # 构建请求参数
    data = {
        'type': 'pdd.ddk.goods.detail',
        'data_type': 'JSON',
        'timestamp': 'your_timestamp',
        'client_id': app_key,
        'access_token': 'your_access_token',
        'sign': '',
        'goods_id': 'your_goods_id'
    }

    # 计算签名
    md5 = hashlib.md5()
    sign_str = app_secret
    for key in sorted(data.keys()):
        sign_str += key + str(data[key])
    sign_str += app_secret
    md5.update(sign_str.encode('utf-8'))
    sign = md5.hexdigest().upper()
    data['sign'] = sign

    # 发送API请求
    response = requests.post(api_url, data=data)

    # 处理API响应
    if response.status_code == requests.codes.ok:
        response_data = json.loads(response.text)
        if response_data.get('error_code') is not None:
            print('API Error: ' + response_data['error_msg'])
        else:
            goods_detail = response_data['goods_detail_response']['goods_details'][0]
            print('商品名称：' + goods_detail['goods_name'])
            print('商品价格：' + str(goods_detail['min_group_price'] / 100))
            print('佣金比例：' + str(goods_detail['promotion_rate'] / 10) + '%')
    else:
        print('API Error: ' + response.status_code)