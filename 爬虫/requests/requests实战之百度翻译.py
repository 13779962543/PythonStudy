import requests
import json

if __name__=="__main__":
    post_url = 'https://fanyi.baidu.com/sug'
    headers={
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.80 Safari/537.36 Edg/98.0.1108.43'
    }
    #post请求参数处理，同get请求一至
    data={
        'kw':'dog'
    }
    response=requests.post(url=post_url,data=data,headers=headers)
    #获取数据响应：json()方法返回的是obj
    dic_obj=response.json()
    #持久化存储
    fp=open('./dog.json','w',encoding='utf-8')
    json.dump(dic_obj,fp=fp,ensure_ascii=False)
    print('over')