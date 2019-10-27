from lxml import etree
import urllib.request
import re
import time
import os
import room


def unit(pid):
    #返回单元中的房间数"building.aspx?id=34914&presellid=41853"
    urlbase = "http://zjj.sz.gov.cn/ris/bol/szfdc/"
    url="http://zjj.sz.gov.cn/ris/bol/szfdc/"+pid
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.75 Safari/537.36',
                 'Content-Type':'application/x-www-form-urlencoded'}
    req1 = urllib.request.Request(url=url, headers=headers)
    response1 = urllib.request.urlopen(req1)
    result1 = response1.read().decode('utf-8')
    selector1=etree.HTML(result1, parser=None, base_url=None)
    test=selector1.xpath('//div[@id="divShowBranch"]/a/@href')
    res = []
    for i in range(0,len(test)):
        urli=urlbase+test[i]
        req = urllib.request.Request(url=urli, headers=headers)
        response = urllib.request.urlopen(req)
        result = response.read().decode('utf-8')
        selector = etree.HTML(result, parser=None, base_url=None)
        unitsum = selector.xpath('//td/div/a/@href')
        for i in range(len(unitsum)):
            line= room.room(unitsum[i])
            line.append('\n')
            res+=line
    return res




pid="building.aspx?id=34923&presellid=41915"
unit(pid)
