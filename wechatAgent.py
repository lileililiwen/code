import itchat

# 登录微信
itchat.auto_login(hotReload=True)

# 自动回复好友消息
@itchat.msg_register(itchat.content.TEXT)
def reply_msg(msg):
    return '您好，我是微信助手，我正在处理您的消息：{}'.format(msg.text)

# 发送消息给好友
friend = itchat.search_friends(name='艾伦秀秀')[0]
friend.send('您好，我是微信助手，我正在给您发送一条消息')

# 保持运行状态
itchat.run()