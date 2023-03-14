import os
#可以使用Python的paramiko库来实现SSH连接和远程操作。
import paramiko

# 读取hosts.txt文件中的IP地址和登录信息
with open('hosts.txt') as f:
    hosts = [line.strip().split(',') for line in f]

# 待安装的程序文件名
program_file = 'app.tar.gz'

# 远程主机的用户名和密码
username = 'root'
password = 'password'

# 循环连接远程主机
for host in hosts:
    ip = host[0]
    port = 22
    username = host[1]
    password = host[2]

    # 创建SSH客户端
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    # 连接远程主机
    ssh.connect(ip, port, username, password)

    # 创建SFTP客户端
    sftp = ssh.open_sftp()

    # 上传程序文件
    sftp.put(program_file, program_file)

    # 执行解压命令
    stdin, stdout, stderr = ssh.exec_command(f'tar zxvf {program_file}')

    # 输出结果
    print(f'{ip}: {stdout.read().decode()}')

    # 关闭连接
    ssh.close()