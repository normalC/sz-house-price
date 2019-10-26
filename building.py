from lxml import etree
import urllib.request
import re
import time
import os
import unit



def building(name, pid):
    #返回栋数
    page = 1
    url = pid
    print(url)
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.75 Safari/537.36',
               'Content-Type': 'application/x-www-form-urlencoded'}
    req = urllib.request.Request(url=url, headers=headers)
    response = urllib.request.urlopen(req)
    result = response.read().decode('utf-8')
    selector=etree.HTML(result, parser=None, base_url=None)
    items = selector.xpath('//tr/td/a/@href')
    #print(items)
    res = []
    for i in range(len(items)):
        res+=unit.unit(items[i])
    outline = '\n'.join(res)
    with open("property/test.csv" % name, "w") as myfile:
        myfile.write(outline)


url1='http://zjj.sz.gov.cn/ris/bol/szfdc/projectdetail.aspx?id=19377'
building('name', url1)
