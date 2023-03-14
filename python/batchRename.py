import os

# 指定文件夹路径
folder_path = '/path/to/folder'

# 遍历文件夹下所有文件
for filename in os.listdir(folder_path):
    file_path = os.path.join(folder_path, filename)
    # 新文件名称
    new_name = 'new_filename'
    # 修改文件名称
    os.rename(file_path, os.path.join(folder_path, new_name))