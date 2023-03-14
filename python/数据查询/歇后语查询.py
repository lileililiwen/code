# 歇后语是我国人民在生活实践中创造的一种特殊语言形式。它一般由两个部分构成，前半截是形象的比喻，像谜面，后半截是解释、说明，像谜底，十分自然贴切。在一定的语言环境中，通常说出前半截，“歇”去后半截，就可以领会和猜想出它的本意，所以称它为歇后语。
# http://tools.jb51.net/bianmin/xiehouyu
import requests
from bs4 import BeautifulSoup

def get_riddle_answer(question):
    url = 'https://www.baidu.com/s'
    params = {'wd': question + ' 歇后语'}
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    response = requests.get(url, params=params, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    answer = soup.select_one('#content_left .op_exactqa_s_answer .op_exactqa_detail_s_answer').text.strip()
    return answer

question = '太岁头上动土'
answer = get_riddle_answer(question)
print(f'{question} 的答案是：{answer}')    