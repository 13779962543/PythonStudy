import requests

if __name__=="__main__":
    url='http://images.china.cn/site1000/2022-02/06/3]]42a3643-5a48-4acf-8476-525c5c7bf4ca.jpg'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.80 Safari/537.36 Edg/98.0.1108.43'
    }
    #text(字符串）content(二进制响应数据),json(对象)
    ima_data=requests.get(url=url).content
    with open('./photo.jpg','wb') as fp:
        fp.write(ima_data)
