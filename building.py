from lxml import etree
import urllib.request
import re
import time
import os
import room

def grab_single(pid, page):
    url = url2
    # print(url)
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.75 Safari/537.36',
                 'Content-Type':'application/x-www-form-urlencoded'}
    req = urllib.request.Request(url=url, headers=headers)
    response = urllib.request.urlopen(req)
    result = response.read().decode('utf-8')
    selector=etree.HTML(result, parser=None, base_url=None)
    items = selector.xpath('//tr[@class="tab_body"]/td/text() | //tr[@class="tab_body bd1"]/td/text()')
    lines = [items[i : i + 8] for i in range(0, len(items), 8)]
    res = []
    for line in lines:
        res.append(','.join(line))
    return res

def building(name, pid):
    page = 1
    url = pid
    print(url)
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.75 Safari/537.36',
               'Content-Type': 'application/x-www-form-urlencoded'}
    req = urllib.request.Request(url=url, headers=headers)
    response = urllib.request.urlopen(req)
    result = response.read().decode('utf-8')
    selector=etree.HTML(result, parser=None, base_url=None)
    items = selector.xpath('//div[@id="divShowBranch"]/a/@href')
    print(items)
    for i in range(len(items)):
        print((items(i)))

url='http://zjj.sz.gov.cn/ris/bol/szfdc/building.aspx?id=34963&presellid=41997'
url1='http://zjj.sz.gov.cn/ris/bol/szfdc/building.aspx?id=34914&presellid=41853'
grab_page('name', url)
