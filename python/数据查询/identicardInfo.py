#http://tools.jb51.net/bianmin/sfz
#代码使用了聚合数据API提供的身份证归属地查询接口，需要替换your_app_key为你自己的API密钥。调用该函数并传入身份证号码，即可返回该身份证对应的区域、性别和出生日期等信息。
import requests

def id_card_info(id_card):
    url = "https://apis.juhe.cn/idcard/index"
    params = {
        "cardno": id_card,
        "dtype": "json",
        "key": "your_app_key"
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        if data["error_code"] == 0:
            info = data["result"]
            return info["area"], info["sex"], info["birthday"]
        else:
            return "查询失败"
    else:
        return "查询失败"