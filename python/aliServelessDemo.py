import json
from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.request import CommonRequest
from tablestore import OTSClient, Row, Condition, RowExistenceExpectation


#请注意，您需要使用您自己的阿里云账号信息（accessKeyId，accessSecret 和 regionId）来替换上面代码中的占位符。
# 此外，您还需要根据您的实际情况来设置请求中的 domain、version 和 action_name 等参数。
client = AcsClient('<accessKeyId>', '<accessSecret>', '<regionId>')

otsclient = OTSClient('<endpoint>', '<accessKeyId>', '<accessSecret>', '<instanceName>')

def login(event, context):
    event = json.loads(event)
    username = event['username']
    password = event['password']

    # 验证用户名和密码
    # 查询表格存储中的用户信息
    primary_key = [('username', username)]
    columns_to_get = ['password']
    row = client.get_row('<tableName>', primary_key, columns_to_get).row

    # 验证用户名和密码
    if row and row.primary_key[0][1] == username and row.attribute_columns[0][1] == password:
        return {
            'success': True,
            'message': '登录成功'
        }
        return {
            'success': True,
            'message': '登录成功'
        }
    else:
        return {
            'success': False,
            'message': '用户名或密码错误'
        }

def create_blog(title, content):
    request = CommonRequest()
    request.set_accept_format('json')
    request.set_domain('<domain>')
    request.set_method('POST')
    request.set_protocol_type('https')
    request.set_version('<version>')
    request.set_action_name('<action_name>')

    data = {
        "title": title,
        "content": content
    }

    request.add_body_params('data', json.dumps(data))

    response = client.do_action_with_exception(request)
    return response

def get_blog(id):
    request = CommonRequest()
    request.set_accept_format('json')
    request.set_domain('<domain>')
    request.set_method('GET')
    request.set_protocol_type('https')
    request.set_version('<version>')
    request.set_action_name('<action_name>')
    request.add_query_param('id', id)

    response = client.do_action_with_exception(request)
    return response

def update_blog(id, title, content):
    request = CommonRequest()
    request.set_accept_format('json')
    request.set_domain('<domain>')
    request.set_method('PUT')
    request.set_protocol_type('https')
    request.set_version('<version>')
    request.set_action_name('<action_name>')

    data = {
        "title": title,
        "content": content
    }

    request.add_body_params('data', json.dumps(data))
    request.add_query_param('id', id)

    response = client.do_action_with_exception(request)
    return response

def delete_blog(id): 
    request = CommonRequest()
    request.set_accept_format('json')
    request.set_domain('<domain>')
    request.set_method('DELETE')
    request.set_protocol_type('https')
    request.set_version('<version>')
    request.set_action_name('<action_name>')

    request.add_query_param('id', id)

    response = client.do_action_with_exception(request)
    return response