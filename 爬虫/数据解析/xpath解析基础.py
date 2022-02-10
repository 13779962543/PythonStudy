from lxml import etree

if __name__=="__main__":
    parser=etree.HTMLParser(encoding='utf-8')
    #实例化完成了一个etree对象，且将被解析的源码加载到该对象中
    tree=etree.parse('test.html',parser=parser)
    # r=tree.xpath('/html/head/title')
    # r=tree.xpath('/html//div')#//:表示的是多个层级
    #属性定位://div[@class=""] tag[@attrName="attrValue"]
    # r=tree.xpath('//div[@class="container"]')
    r=tree.xpath('//div[@class="container"]/span/text()')
    print(r)
