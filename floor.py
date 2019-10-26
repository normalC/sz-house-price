from lxml import etree
import urllib.request
import re
import time
import os

def room(pid):
    #获取房子详细信息,输入为类似“id=1696669”的pid
    url="http://zjj.sz.gov.cn/ris/bol/szfdc/"+pid
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.75 Safari/537.36',
                 'Content-Type':'application/x-www-form-urlencoded'}
    req = urllib.request.Request(url=url, headers=headers)
    response = urllib.request.urlopen(req)
    result = response.read().decode('utf-8')
    selector=etree.HTML(result, parser=None, base_url=None)
    items = selector.xpath('//*/td/text()')
    lines = [print(items[i : i + 8]) for i in range(0, len(items), 8)]
    res = []
    for line in lines:
        res.append(','.join(line))
        return res
