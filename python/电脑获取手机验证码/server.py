import socket

# 创建一个socket，绑定到本地IP和端口socket.AF_INET 和 socket.SOCK_STREAM 是 Python 中 socket 模块中的两个常量。

# socket.AF_INET 表示使用 IPv4 协议族。

# socket.SOCK_STREAM 表示使用基于 TCP 的流式套接字。

# 在 Python 中使用 socket 模块进行网络编程时，常常需要使用这两个常量来指定网络协议类型和套接字类型。例如，socket.socket(socket.AF_INET, socket.SOCK_STREAM) 创建一个 IPv4 的 TCP 套接字。

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('0.0.0.0', 8888))
# 表示让服务器套接字 s 监听传入连接请求队列的大小，即最多能够接受多少个未决连接请求。当服务器套接字收到客户端的连接请求时，如果未决连接请求数已经达到上限，那么服务器会拒绝新的连接请求。如果未决连接请求数还没有达到上限，那么服务器就会将新的连接请求放入队列中等待处理。listen() 方法只有在服务器套接字被绑定到某个地址并且处于监听状态时才能调用。
s.listen(5)

while True:
    # 接受客户端连接
    client, addr = s.accept()
    print(f'Connected by {addr}')

    # 接收验证码
    data = client.recv(1024)
    print('Received:', data.decode())

    client.close()