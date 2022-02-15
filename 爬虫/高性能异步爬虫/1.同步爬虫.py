import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.80 Safari/537.36 Edg/98.0.1108.43'
}
urls={
    'https://www.chaoxing.com/',
    'http://www.chaojiying.com/api-14.html',
}

def get_content(url):
    print('正在爬取:',url)
    respond=requests.get(url=url,headers=headers)
    if respond.status_code==200:
        return respond.content

def parse_content(content):
    print('响应数据的长度为：',len(content))


for url in urls:
    content=get_content(url)
    parse_content(content)
