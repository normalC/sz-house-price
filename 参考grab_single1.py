from lxml import etree
import urllib.request
import re
import time
import os

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

def grab_page(name, pid):
    page = 1
    url = pid
    print(url)
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.75 Safari/537.36',
               'Content-Type': 'application/x-www-form-urlencoded'}
    req = urllib.request.Request(url=url, headers=headers)
    response = urllib.request.urlopen(req)
    result = response.read().decode('utf-8')
    selector=etree.HTML(result, parser=None, base_url=None)
    print(selector)
    items = selector.xpath('//*/td/a/@href')
    #print(items)
    for i in range(len(items)):
        print("http://zjj.sz.gov.cn/ris/bol/szfdc/"+items[i])
    lines = [items[i : i + 8] for i in range(0, len(items), 8)]
    res = []
    for line in lines:
        res.append(','.join(line))
    return res
    print(res)
    page_span = selector.xpath('//td/a/text()')
    print(page_span )
    page_num = int(page_span[0].split('/')[1])
    print(pid)
    print(page_num)
    res = []
    for page in range(1, page_num + 1):
    # for page in range(1, 5 + 1):
        res += grab_single(pid, page)
    outline = '\n'.join(res)
    outline = "房号,建筑面积,建筑面积单价,套内面积,套内面积单价,总售价,销售状况,备注\n" + outline
    with open("property/%s.csv" % name, "w") as myfile:
        myfile.write(outline)

'''rdlines = open('properties.csv').readlines()

for line in rdlines[:]:
    item = line.split(',')
    name = item[1]
    pid = item[-1][:-1]
    #print(name, pid)
    if os.path.isfile("property/%s.csv" % name):
        continue
    try:
        grab_page(name, pid)
    except:
        pass
'''
url='http://zjj.sz.gov.cn/ris/bol/szfdc/projectdetail.aspx?id=41853'
url2='http://zjj.sz.gov.cn/ris/bol/szfdc/building.aspx?id=34914&presellid=41853'
grab_page('name', url)
