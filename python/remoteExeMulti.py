import paramiko
import threading
import queue
import sys

def execute_command(ip, username, password, command):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        ssh.connect(ip, username=username, password=password, timeout=5)
        stdin, stdout, stderr = ssh.exec_command(command)
        for line in stdout:
            print(line.strip('\n'))
        ssh.close()
    except Exception as e:
        print('Error: %s %s' % (ip, e))

if __name__ == '__main__':
    username = input('Enter your username: ')
    password = input('Enter your password: ')
    command = input('Enter your command: ')

    ips = ['192.168.1.101', '192.168.1.102', '192.168.1.103']
    threads = []
    for ip in ips:
        t = threading.Thread(target=execute_command, args=(ip, username, password, command))
        t.start()
        threads.append(t)

    for t in threads:
        t.join()