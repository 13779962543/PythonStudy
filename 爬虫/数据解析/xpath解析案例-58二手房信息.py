import requests
from lxml import etree

if __name__=="__main__":
    parser = etree.HTMLParser(encoding='utf-8')
    #爬取到页面源代码数据
    url='https://bj.58.com/ershoufang/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.80 Safari/537.36 Edg/98.0.1108.43'
    }
    page_text=requests.get(url=url,headers=headers).text
    #数据解析
    tree=etree.HTML(page_text,parser=parser)
    #储存的就是h3标签的对象
    li_list=tree.xpath('//div[@class="property-content-title"]')
    fp=open('58.txt','w',encoding='utf-8')
    for li in li_list:
        title=li.xpath('./h3/text()')[0]
        print(title)
        fp.write(title+'\n')
