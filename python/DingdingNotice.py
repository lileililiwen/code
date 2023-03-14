import requests
import json
import hmac
import hashlib
import base64
from urllib import parse
import time

WEBHOOK = 'your_webhook'
SECRET = 'your_secret'

def send_text_message(webhook, secret, content):
    timestamp = str(round(time.time() * 1000))
    secret_enc = secret.encode('utf-8')
    string_to_sign = '{}\n{}'.format(timestamp, secret)
    string_to_sign_enc = string_to_sign.encode('utf-8')
    hmac_code = hmac.new(secret_enc, string_to_sign_enc, digestmod=hashlib.sha256).digest()
    sign = parse.quote_plus(base64.b64encode(hmac_code))
    url = f'{webhook}&timestamp={timestamp}&sign={sign}'
    
    headers = {'Content-Type': 'application/json'}
    data = {
        "msgtype": "text",
        "text": {
            "content": content
        }
    }
    
    res = requests.post(url, data=json.dumps(data), headers=headers)
    print(res.text)

# 在上面的代码中，你需要将 WEBHOOK 和 SECRET 替换为你自己的钉钉群聊机器人相关信息。然后运行这段代码，就可以在指定的群聊中看到发送的消息了。
if __name__ == '__main__':
    send_text_message(WEBHOOK, SECRET, 'Hello from Python!')