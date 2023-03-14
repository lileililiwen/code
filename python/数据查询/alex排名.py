import requests
import json

#http://tools.jb51.net/aideddesign/alexa
# 这是一款可查询Alexa网站排名的工具，可查询网站的世界排名、国内/地区排名、访客排名等数据！方便站长对网站信息进行查询，提供给需要的朋友参考使用。
# Alexa API请求地址
url = 'https://awis.api.alexa.com/api?Action=UrlInfo&ResponseGroup=Rank&Url='

# 请求参数
access_key = 'YOUR_ACCESS_KEY_HERE'
secret_key = 'YOUR_SECRET_KEY_HERE'
site = 'www.example.com'

# 拼接请求URL
request_url = url + site

# 添加签名认证信息
headers = {'Content-Type': 'application/json',
           'x-amz-date': '20220313T104111Z',
           'Authorization': 'AWS4-HMAC-SHA256 Credential=' + access_key + '/20220313/us-east-1/awis/aws4_request, SignedHeaders=content-type;host;x-amz-date, Signature=cf7cb0ff9dd2a7f8b29d0ebd71a42417487d04cb1ba81aa44029d17bdf9d23de'}

# 发送请求
response = requests.get(request_url, headers=headers)

# 解析返回的JSON格式数据
response_data = json.loads(response.content)

# 输出目标网站的排名信息
rank = response_data['Alexa']['TrafficData']['Rank']
print("目标网站排名: " + rank)