import os
import requests
from lxml import etree

# 搜索关键词
keyword = "周杰伦"

# 搜索 URL
search_url = "http://www.kugou.com/yy/html/search.html"

# 音乐列表 URL 模板
list_url_template = "http://www.kugou.com/yy/html/search.html#searchType=song&searchKeyWord={keyword}&page={page}"

# 音乐下载 URL 模板
download_url_template = "http://www.kugou.com/yy/index.php?r=play/getdata&hash={hash}&album_id={album_id}"

# 创建目录
if not os.path.exists(keyword):
    os.mkdir(keyword)

# 搜索

response = requests.post(search_url, data={"keyword": keyword})
dir(response)

html = etree.HTML(response.text)

# 获取音乐列表总页数
total_pages = int(html.xpath('//div[@class="page"]/a[last()-1]/text()')[0])

# 遍历每一页
for page in range(1, total_pages + 1):
    print(f"正在处理第 {page} 页...")

    # 获取音乐列表
    list_url = list_url_template.format(keyword=keyword, page=page)
    print(list_url)
    response = requests.get(list_url)
    html = etree.HTML(response.text)

    # 遍历每首音乐
    for song in html.xpath('//div[@class="search_result_song"]/div[@class="songname"]/a'):

        # 获取音乐名称和 ID
        name = song.xpath('./text()')[0]
        id = song.xpath('./@href')[0].split("/")[-1].split(".")[0]

        # 获取音乐下载链接
        download_url = download_url_template.format(hash=id, album_id=0)
        response = requests.get(download_url)
        data = response.json()["data"]
        url = data["play_url"]

        # 下载音乐
        filepath = os.path.join(keyword, f"{name}.mp3")
        response = requests.get(url, stream=True)
        with open(filepath, "wb") as f:
            for chunk in response.iter_content(chunk_size=1024):
                if chunk:
                    f.write(chunk)

print("全部下载完成！")