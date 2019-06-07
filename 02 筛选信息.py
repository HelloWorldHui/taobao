# coding=utf
"""
author=Hui_T
"""
from lxml import etree
with open("taobao.html","r",encoding="utf8") as f:
    tree = etree.HTML(f.read())
ret = tree.xpath('//*[@id="mainsrp-itemlist"]/div/div/div[1]/div')
for element in ret:
    price = "￥"+element.xpath('div[2]/div[1]/div[1]/strong/text()')[0]
    name = ",".join([ i.strip() for i in element.xpath('div[2]/div[2]/a/text()') if  i.strip()!=''])
    sales = element.xpath('div[2]/div[1]/div[2]/text()')[0]
    print(price,name,sales)