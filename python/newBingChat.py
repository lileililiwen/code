import requests
import json
import time
import hashlib

####新bing人工聊天机器人
def newbing_chat(appkey,appsecret,question):
    url = 'https://api.newbing.net/olami/v1/chatbot'
    api = 'chatbot'
    timestamp = str(int(time.time()))
    sign = hashlib.md5((api+appkey+timestamp+appsecret).encode())
    data = {
        'appkey': appkey,
        'timestamp': timestamp,
        'sign': sign,
        'api': api,
        'question': question
    }
    response = requests.post(url, data=data)
    result = json.loads(response.text)
    return result['data']['answer']

appKey=""
appsecret=""
question = input('请输入您的问题：')
answer = newbing_chat(appKey,appsecret,question)
print('Newbing回答：', answer)