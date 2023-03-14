from fbchat import Client
from fbchat.models import *

# 首先，你需要通过 Facebook Developers 网站创建一个应用程序，并获取 email 和 password
email = 'your_email'
password = 'your_password'

# 使用 email 和 password 登录 Facebook 账号
client = Client(email, password)

# 获取要发送消息的所有好友列表
friends = ['friend_1', 'friend_2', 'friend_3'] # 好友列表

# 发送消息
for friend in friends:
    friend_list = client.searchForUsers(friend)
    if friend_list:
        friend_id = friend_list[0].uid
        message = 'Hello, ' + friend + '!'
        sent = client.sendMessage(message, thread_id=friend_id, thread_type=ThreadType.USER)
        if sent:
            print('Message sent to', friend)
    else:
        print('Could not find', friend, 'on Facebook')

# 退出账号
client.logout()

# 这个代码使用了 fbchat 库，通过 email 和 password 登录 Facebook 账号，然后发送指定好友列表的消息。注意，你需要使用自己的 email 和 password 替换代码中的 your_email 和 your_password，
# 并将 ['friend_1', 'friend_2', 'friend_3'] 替换为你要发送消息的好友列表。在消息发送成功后，代码会打印消息已发送的提示。你也可以根据自己的需要调整代码来实现其他 Facebook Messenger 的操作