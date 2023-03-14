import os
import shutil

### 文件操作 ###

# 创建文件
with open("test.txt", "w") as f:
    f.write("Hello, world!")

# 读取文件
with open("test.txt", "r") as f:
    content = f.read()
    print(content)

# 追加内容
with open("test.txt", "a") as f:
    f.write("\nHello again!")

# 复制文件
shutil.copyfile("test.txt", "test_copy.txt")

# 删除文件
os.remove("test.txt")

### 文件夹操作 ###

# 创建文件夹
os.mkdir("test_dir")

# 遍历文件夹
for root, dirs, files in os.walk("test_dir"):
    print(f"当前目录：{root}")
    print(f"子目录：{dirs}")
    print(f"文件：{files}")

# 复制文件夹
shutil.copytree("test_dir", "test_dir_copy")

# 删除文件夹
shutil.rmtree("test_dir")