import requests
#UA伪装
#UA User-Agent：（请求载体的身份标识）

if __name__=="__main__":
    #UA伪装,将对应的请求载体身份标识封装到一个字典中
    headers={
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.80 Safari/537.36 Edg/98.0.1108.43'
    }
    url='https://www.sogou.com/web'
    kw=input("enter a word:")

    param={
        'query':kw
    }
    response=requests.get(url=url,params=param,headers=headers)
    page_text=response.text
    fileName=kw+'.html'
    with open(fileName,'w',encoding='utf-8') as fp:
        fp.write(page_text)
    print(fileName,'保存成功')