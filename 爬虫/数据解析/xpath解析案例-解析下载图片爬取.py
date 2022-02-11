import os
import requests
from lxml import etree
import urllib.request

if __name__=="__main__":

    url='https://pic.netbian.com/4kmeinv/'

    # 循环输出页数


    print(url)
    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.80 Safari/537.36 Edg/98.0.1108.43'
    }
    response=requests.get(url=url,headers=headers)
    #手动设定响应数据的编码格式
    response.encoding=response.apparent_encoding
    data=response.text
    #数据解析:src属性值，alt属性值
    tree=etree.HTML(data)
    li_list=tree.xpath('//div[@class="slist"]/ul/li')
    if not os.path.exists('./beautifulgirl'):
        os.mkdir('./beautifulgirl')
    for li in li_list:
        img_src='https://pic.netbian.com/'+li.xpath('./a/img/@src')[0]
        img_name=li.xpath('./a/img/@alt')[0]+'.jpg'
        #通用处理中文乱码的解决方法
        # img_name=img_name.encode('iso-8859-1').decode('gbk')
        #请求图片进行持久化处理
        img_data=requests.get(url=img_src,headers=headers).content
        img_path='beautifulgirl/'+img_name
        with open(img_path,'wb')as fp:
            fp.write(img_data)
            print(img_name,'下载成功')


