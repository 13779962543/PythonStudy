import re

import requests
import os

if __name__=="__main__":
    #创建一个文件用来保存图片
    if not os.path.exists('./qiutuLibs'):
        os.mkdir('./qiutuLibs')

    url='https://www.dbbqb.com/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.80 Safari/537.36 Edg/98.0.1108.43'
    }
    #使用通用爬虫对url对应的一整张页面进行爬取
    page_text=requests.get(url=url,headers=headers).text
    #使用聚焦爬虫将页面中所有的图片进行爬取
    ex='<div class="lazyload-wrapper">.*?<img class="jss51" src="(.*?)" alt.*?</div>'
    img_src_list=re.findall(ex,page_text,re.S)

    for src in img_src_list:
        #拼接出一个完整的图片
        src='https:'+src
        #请求到了图片的二进制数据
        img_data=requests.get(url=src,headers=headers).content

        #生成图片名称
        img_name=src.split('/')[-1]
        #图片存储的路劲
        imgPath='./qiutuLibs'+img_name
        with open(imgPath,'wb') as fp:
            fp.write(img_data)
            print(img_name,'下载成功')

