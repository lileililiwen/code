import os
import requests
from bs4 import BeautifulSoup

def download_doc(url, path):
    """下载文档"""
    response = requests.get(url)
    file_name = url.split('/')[-1]
    file_path = os.path.join(path, file_name)
    with open(file_path, 'wb') as f:
        f.write(response.content)

def search_docs(keyword):
    """搜索文档"""
    page_num = 1
    path = './docs'  # 存储文件夹路径
    if not os.path.exists(path):
        os.mkdir(path)
    while True:
        url = 'https://wenku.baidu.com/search?word={}&lm=0&od=0&fr=top_home&ie=gbk&page={}'.format(keyword, page_num)
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        docs = soup.find_all('a', class_='log-click')
        if not docs:
            break  # 没有搜索结果，停止搜索
        for doc in docs:
            doc_url = doc['href']
            if doc_url.endswith('.doc') or doc_url.endswith('.docx') or doc_url.endswith('.pdf'):
                download_doc(doc_url, path)
        page_num += 1

# 这段代码会从第1页开始搜索关键词为“python”的文档，每页下载所有doc、docx和pdf类型的文档，并将它们保存到./docs文件夹中，文件名与原始文件相同。
if __name__ == '__main__':
    keyword = 'python'  # 搜索关键词
    search_docs(keyword)