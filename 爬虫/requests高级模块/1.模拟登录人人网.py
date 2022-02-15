# 1.验证码的识别，获取图片的文字数据
# 2.对post请求进行发送（处理请求参数）
# 3.对响应数据进行持久化储存
import requests
from lxml import etree
from chaojiying import Chaojiying_Client

#1.对验证码图片进行捕获和识别
url_main='https://passport2.chaoxing.com/login?fid=&refer='
headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.80 Safari/537.36 Edg/98.0.1108.43'
    }
page_text=requests.get(url=url_main,headers=headers).text
tree=etree.HTML(page_text)
# code_img_src=tree.xpath('//*[@id="numVerCode"]/@src')[0]
#
# print(code_img_src)
# url='https://passport2.chaoxing.com'+code_img_srcr
# code_img_data=requests.get(url=url,headers=headers).content
# with open('./code.jpg','wb') as fp:
#     fp.write(code_img_data)
# #初始化超级鹰
# chaojiying=Chaojiying_Client('13779962543', 'wxb823419', '919838')
# dic=chaojiying.PostPic('code.jpg',9004)

url='https://passport2.chaoxing.com/fanyalogin'
data={
    'fid': '-1',
    'uname': '13779962543',
    'password': 'd3hiODIzNDE5',
    'refer': 'http%3A%2F%2Fi.chaoxing.com',
    't': 'true',
    'forbidotherlogin': '0',
    'validate': '',
}
