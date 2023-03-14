import firebase_admin
from firebase_admin import credentials, firestore

# 初始化 Firebase 应用
cred = credentials.Certificate('path/to/credentials.json')
firebase_admin.initialize_app(cred)

# 获取 Firestore 数据库实例
db = firestore.client()
print("db"+db)

# 添加博客
def add_blog(title, content):
    blogs_ref = db.collection('blogs')
    blogs_ref.add({
        'title': title,
        'content': content
    })
    print('博客已添加')

# 获取所有博客
def get_blogs():
    blogs_ref = db.collection('blogs')
    docs = blogs_ref.stream()
    blogs = []
    for doc in docs:
        blog = doc.to_dict()
        blog['id'] = doc.id
        blogs.append(blog)
    return blogs

# 获取单个博客
def get_blog(id):
    blog_ref = db.collection('blogs').document(id)
    doc = blog_ref.get()
    if doc.exists:
        blog = doc.to_dict()
        blog['id'] = doc.id
        return blog
    else:
        return None

# 更新博客
def update_blog(id, title, content):
    blog_ref = db.collection('blogs').document(id)
    blog_ref.update({
        'title': title,
        'content': content
    })
    print('博客已更新')

# 删除博客
def delete_blog(id):
    blog_ref = db.collection('blogs').document(id)
    blog_ref.delete()
    print('博客已删除')


# 添加博客
add_blog('第一篇博客', '这是我的第一篇博客。')

# 获取所有博客
blogs = get_blogs()
for blog in blogs:
    print(blog['title'], blog['content'])

# 获取单个博客
blog = get_blog('xxxxx')
if blog:
    print(blog['title'], blog['content'])
else:
    print('博客不存在')

# 更新博客
update_blog('xxxxx', '新标题', '新内容')

# 删除博客
delete_blog('xxxxx')    