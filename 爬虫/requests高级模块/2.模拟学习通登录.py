import requests
from lxml import etree

url_main='https://passport2.chaoxing.com/login?fid=&refer='
headers = {
       'Cookie':'JSESSIONID=67165302FB151FCF2A452394716CF5A2; route=3a66e47c0ac92560e5c67cd5e1803201; source=""; spaceFid=20614; spaceRoleId=""; lv=1; fid=20614; _uid=157639109; uf=da0883eb5260151ebad017f8c21b74bd8250d4bc72bda767ad03318e0d1ae11e6f0b3d2d797f584244eae6da7b6242fef6a6e9008e9900b988b83130e7eb47043d60939e5db592aa4a2957972c9cfec64129e2925200b376185090f13059192eaead904cf5288b16e7fafd565af53bf2; _d=1644677202120; UID=157639109; vc=3AA3F159E7AFBD9EFD3B894E5C039CBA; vc2=9E2D3C2D7FA8F84D07D4C3CD5C90289B; vc3=dt9PQ2COzoHz1G6Gay1cmsOnLvv0yEnT70MkKFoKl9XrW6S1mFJoLk1eqJymwoWIa6yqRc++XvGDqGMlvxB/pRGFFNjz6aFfTuDO02hdZEjtRQfCj2bF4FnxLNmQS87Rv19RepketIJd8pD7QheTH2x5sIIUNsyARpwijD/4QAA=5446746a73606bd766706f081f62d992; xxtenc=e3a7f9326aeacf092a60ae2259bce669; DSSTASH_LOG=C_38-UN_21729-US_157639109-T_1644677202122'
    }
page_text=requests.get(url=url_main,headers=headers).text
tree=etree.HTML(page_text)

detail_url='http://i.chaoxing.com/base?t=1644677234061'
detail_page_test=requests.get(url=detail_url,headers=headers).text
with open('xiaobai.html','w',encoding='utf-8') as fp:
    fp.write(detail_page_test)