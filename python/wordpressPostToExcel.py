import openpyxl
import requests

# 定义WordPress站点地址、用户名和密码
wordpress_url = 'https://example.com/wp-json/wp/v2/'
wordpress_username = 'your_username'
wordpress_password = 'your_password'

# 获取所有文章的数据
response = requests.get(wordpress_url + 'posts', auth=(wordpress_username, wordpress_password))
all_posts = response.json()

# 创建Excel文件
workbook = openpyxl.Workbook()
worksheet = workbook.active

# 添加表头
worksheet.append(['ID', '标题', '作者', '发布时间', '文章链接'])

# 添加数据
for post in all_posts:
    post_id = post['id']
    post_title = post['title']['rendered']
    post_author = post['author']
    post_date = post['date']
    post_link = post['link']
    worksheet.append([post_id, post_title, post_author, post_date, post_link])

# 保存Excel文件
workbook.save('wordpress_posts.xlsx')