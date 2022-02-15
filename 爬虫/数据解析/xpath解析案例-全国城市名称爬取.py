import requests
from lxml import etree

if __name__=="__main__":
    # headers = {
    #     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.80 Safari/537.36 Edg/98.0.1108.43'
    # }
    # url='http://www.aqistudy.cn/historydata/'
    # page_text=requests.get(url=url,headers=headers).text
    # tree=etree.HTML(page_text)
    # host_li_list=tree.xpath('//div[@class="bottom"]/ul/li')
    # all_city_names=[]
    # #解析到了热门城市的城市名称
    # for li in host_li_list:
    #     host_city_name=li.xpath('./a/text()')[0]
    #     all_city_names.append(host_city_name)
    # city_names_list=tree.xpath('//div[@class="bottom"]/ul/div[2]/li')
    # #解析全部城市的名称
    # for li in city_names_list:
    #     city_name=li.xpath('./a/text()')[0]
    #     all_city_names.append(city_name)
    # print(all_city_names,len(all_city_names))

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.80 Safari/537.36 Edg/98.0.1108.43'
    }
    url = 'http://www.aqistudy.cn/historydata/'
    page_text = requests.get(url=url, headers=headers).text
    tree = etree.HTML(page_text)
    #解析到热门城市和所有城市对应的a标签
    # div/ul/li/a   热门城市
    # div/ul/div[2]/li/a 全部城市
    a_list=tree.xpath('//div[@class="bottom"]/ul/li/a | //div[@class="bottom"]/ul/div[2]/li/a')
    all_city_names=[]
    for a in a_list:
        city_name=a.xpath('./text()')[0]
        all_city_names.append(city_name)
    print(all_city_names)

