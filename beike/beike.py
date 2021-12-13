from lxml import etree
import urllib.request
import re
import time
import os
import unit



def building(name, pid):
    #返回栋数
    url = pid+name
    #print(url)
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.75 Safari/537.36',
               'Content-Type': 'application/x-www-form-urlencoded'}
    req = urllib.request.Request(url=url, headers=headers)
    #print(req)
    response = urllib.request.urlopen(req)
    #print(response)
    result = response.read().decode('utf-8')
    print(result)
    selector=etree.HTML(result, parser=None, base_url=None)
    print(selector)
    items = selector.xpath('//tr/td/a/@href')
    #print(items)
    res = []
    for i in range (len(items)):
        #print(items[i])
        res+=unit.unit(items[i])
    outline = ''.join(res)
    with open("property/%s.csv" % name, "w") as myfile:
        myfile.write(outline)



rdlines = open('ershou.csv').readlines()
for line in rdlines[:]:
    item = line.split(',')
    name = item[-1][:-1]    
    pid= item[0]
    if os.path.isfile("property/%s.csv" % name):
        continue
    try:
        #print("test")
        building(name, pid)
    except:
        pass

# pid="projectdetail.aspx?id=77965"
# building("test",pid)
