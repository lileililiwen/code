import os
import paramiko

class SFTPClient:
    def __init__(self, host, port, username, password):
        self.host = host
        self.port = port
        self.username = username
        self.password = password
        self.transport = paramiko.Transport((self.host, self.port))
        self.transport.connect(username=self.username, password=self.password)
        self.sftp = paramiko.SFTPClient.from_transport(self.transport)

    def change_directory(self, directory):
        self.sftp.chdir(directory)

    def download_file(self, remote_file_path, local_file_path):
        self.sftp.get(remote_file_path, local_file_path


import ftplib
import os

class FTPClient:
    def __init__(self, host, username, password):
        self.host = host
        self.username = username
        self.password = password
        self.ftp = ftplib.FTP(self.host, self.username, self.password)

    def change_directory(self, directory):
        self.ftp.cwd(directory)

    def download_file(self, remote_file_path, local_file_path):
        with open(local_file_path, 'wb') as f:
            self.ftp.retrbinary('RETR ' + remote_file_path, f.write)

    def upload_file(self, local_file_path, remote_file_path):
        with open(local_file_path, 'rb') as f:
            self.ftp.storbinary('STOR ' + remote_file_path, f)

    def download_directory(self, remote_directory_path, local_directory_path):
        os.makedirs(local_directory_path, exist_ok=True)
        self.change_directory(remote_directory_path)
        for item in self.ftp.nlst():
            if self.is_directory(item):
                self.download_directory(item, os.path.join(local_directory_path, item))
            else:
                self.download_file(item, os.path.join(local_directory_path, item))

    def upload_directory(self, local_directory_path, remote_directory_path):
        self.ftp.mkd(remote_directory_path)
        self.change_directory(remote_directory_path)
        for item in os.listdir(local_directory_path):
            local_item_path = os.path.join(local_directory_path, item)
            remote_item_path = os.path.join(remote_directory_path, item)
            if os.path.isfile(local_item_path):
                self.upload_file(local_item_path, remote_item_path)
            elif os.path.isdir(local_item_path):
                self.upload_directory(local_item_path, remote_item_path)

    def delete_file(self, remote_file_path):
        self.ftp.delete(remote_file_path)

    def rename_file(self, remote_file_path, new_name):
        self.ftp.rename(remote_file_path, new_name)

    def create_directory(self, remote_directory_path):
        self.ftp.mkd(remote_directory_path)

    def delete_directory(self, remote_directory_path):
        for item in self.ftp.nlst(remote_directory_path):
            if self.is_directory(item):
                self.delete_directory(item)
            else:
                self.delete_file(item)
        self.ftp.rmd(remote_directory_path)

    def disconnect(self):
        self.ftp.quit()

    def is_directory(self, item):
        try:
            self.ftp.cwd(item)
            self.ftp.cwd('..')
            return True
        except:
            return False

            