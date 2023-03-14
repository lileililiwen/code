import requests

# 本工具是名人名言查询工具。一名人名言指名人所说的话，广泛上来说是比较有名的话与有意义的话，名人所说的谚语，格言等都可以叫名人名言。搜录了大量的名人名言供用户查询。
# http://tools.jb51.net/bianmin/mingyan
def get_famous_quote(keyword):
    url = 'https://v1.hitokoto.cn/nm/search/quote?keyword={}&page=1&per_page=10'.format(keyword)
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if data['result']:
            quote = data['result'][0]['content']
            author = data['result'][0]['source']
            return quote, author
    return None, None

if __name__ == '__main__':
    keyword = input('请输入关键字：')
    quote, author = get_famous_quote(keyword)
    if quote and author:
        print('名言：{}'.format(quote))
        print('作者：{}'.format(author))
    else:
        print('没有找到相关名言')