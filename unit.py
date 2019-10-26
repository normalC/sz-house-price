from lxml import etree
import urllib.request
import re
import time
import os
import room


def unit(pid):
    #返回单元中的房间数"building.aspx?id=34914&presellid=41853"
    url = "http://zjj.sz.gov.cn/ris/bol/szfdc/"+pid
    print(url)
    # print(url)
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.75 Safari/537.36',
                 'Content-Type':'application/x-www-form-urlencoded'}
    req = urllib.request.Request(url=url, headers=headers)
    response = urllib.request.urlopen(req)
    result = response.read().decode('utf-8')
    selector=etree.HTML(result, parser=None, base_url=None)
    unitsum = selector.xpath('//tr/td/div/a/@href')
    #print(unitsum)
    res = []
    for i in range(len(unitsum)):
       line= room.room(unitsum[i])
       line.append('\n')
       print(line)
       res+=line
    print(res)
    return res




pid="building.aspx?id=34914&presellid=41853"
unit(pid)
