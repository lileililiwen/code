import pyeverything as pe
import os

# 搜索关键词
query = "example"

# 搜索文件和文件夹
results = pe.search(query, file=True, folder=True)

# 获取结果路径的绝对路径
abs_results = [os.path.abspath(result['path']) for result in results]

# 按文件大小排序
sorted_results = sorted(abs_results, key=lambda x: os.path.getsize(x), reverse=True)

# 输出结果
for result in sorted_results:
    print(result)


path = "/path/to/search/dir"
results = pe.search(query, file=True, folder=True, path=path)    