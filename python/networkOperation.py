import requests

# 发送 GET 请求并获取响应
response = requests.get('https://www.example.com')
print(response.text)

# 发送 POST 请求并获取响应
data = {'username': 'user1', 'password': '123456'}
response = requests.post('https://www.example.com/login', data=data)
print(response.text)



import socket

# 建立连接并发送数据
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('www.example.com', 80))
request = 'GET / HTTP/1.1\r\nHost: www.example.com\r\n\r\n'
s.send(request.encode())

# 接收响应并解析数据
response = s.recv(1024)
print(response.decode())

# 关闭连接
s.close()


from flask import Flask, request, jsonify

app = Flask(__name__)

# 定义路由及处理方法
@app.route('/')
def index():
    return 'Hello, World!'

@app.route('/api/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data['username']
    password = data['password']
    if username == 'user1' and password == '123456':
        return jsonify({'success': True})
    else:
        return jsonify({'success': False, 'message': 'Invalid username or password'})

# 启动应用
if __name__ == '__main__':
    app.run()



import socketserver

# 定义请求处理类
class MyTCPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        # 接收数据并回应
        data = self.request.recv(1024).strip()
        print("{} wrote:".format(self.client_address[0]))
        print(data.decode())
        response = b'Hello, World!\n'
        self.request.sendall(response)

# 创建服务器并启动
if __name__ == "__main__":
    HOST, PORT = "localhost", 9999
    server = socketserver.TCPServer((HOST, PORT), MyTCPHandler)
    server.serve_forever()    