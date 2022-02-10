import requests
from bs4 import BeautifulSoup
if __name__=="__main__":

    #对首页的页面数据进行爬取
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.80 Safari/537.36 Edg/98.0.1108.43'
    }
    url='https://www.shicimingju.com/book/sanguoyanyi.html'
    response=requests.get(url=url,headers=headers)
    response.encoding = response.apparent_encoding
    data=response.text

    #在首页中解析出章节的标题和详情页的url
    #1.实例化BeautifulSoup对象，需要将页面源码数据加载到该对象
    soup=BeautifulSoup(data,'lxml')
    li_list=soup.select('.book-mulu>ul>li')
    fp=open('./三国演义.txt','w',encoding='utf-8')
    for li in li_list:
        title = li.a.string
        url = 'https://www.shicimingju.com' + li.a['href']

        # 对详情页面发起请求，解析出章节内容
        response = requests.get(url=url, headers=headers)
        response.encoding = response.apparent_encoding
        data = response.text
        # 解析出详情也相关的章节内容
        soup = BeautifulSoup(data, 'lxml')
        div_tag = soup.find('div', class_='chapter_content')
        # 解析到章节内容
        content = div_tag.text
        fp.write(title + ':' + content + '\n')
        print(title, '爬取成功')
