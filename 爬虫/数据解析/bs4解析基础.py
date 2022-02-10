from bs4 import BeautifulSoup

if __name__=="__main__":
    #将本地的html文档的数据加载到该对象中
    fp=open('./test.html','r',encoding='utf-8')
    soup=BeautifulSoup(fp,'lxml')
    # print(soup)
    soup.tagName #返回的是文档中第一次出现tagName对应的标签
    soup.find() #find('tagName'):等同于soup.div
    soup.find_all() #('tagName'):返回符合要求的所有标签（列表）
    # select('某种选择器(id，class，标签...选择器)'),返回的是一个列表