import pdfkit
from urllib.parse import urlparse


def get_base_tag(url):
    base_url = '{uri.scheme}://{uri.netloc}'.format(uri=urlparse(url))
    if not base_url.endswith('/'):
        base_url += '/'
    path = urlparse(url).path
    if path.endswith('/'):
        path = path[:-1]
    base_tag = '<base href="{0}{1}/">'.format(base_url, path)
    return base_tag


def convert_to_pdf(urls, output_file):
    # Join all HTML files into a single HTML string
    html = ''
    for url in urls:
        base_tag = get_base_tag(url)
        html += base_tag
        html += '<iframe src="{0}" style="width:100%;height:100%"></iframe>'.format(url)

    # Convert HTML to PDF using pdfkit
    pdfkit.from_string(html, output_file)


# Example usage
urls = ['https://www.baidu.com']
output_file = 'articles.pdf'
convert_to_pdf(urls, output_file)

# 上面的代码将博客地址存储在一个列表中，并通过循环遍历每个地址。对于每个地址，它使用 get_base_tag 函数来生成相应的 <base> 标签，然后将 <base> 标签和 <iframe> 标签添加到 HTML 字符串中。最后，它将 HTML 字符串传递给 pdfkit.from_string 函数来生成 PDF 文件。

# 请注意，这里假设所有博客页面都可以通过 <iframe> 标签加载，并且它们不需要任何身份验证或其他特殊的处理。如果博客页面需要身份验证或其他特殊处理，请在加载每个页面之前执行相应的操作。