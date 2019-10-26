from lxml import etree
import urllib.request
import re
import time

'def grab_page(page):'
def grab_page():
    url = "http://zjj.sz.gov.cn/ris/bol/szfdc/"
    print(url)
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.75 Safari/537.36'}  
    req = urllib.request.Request(url=url, headers=headers)  
    response = urllib.request.urlopen(req)
    result = response.read().decode('utf-8')
    selector=etree.HTML(result, parser=None, base_url=None)
    companys = selector.xpath('//tr[@class=""]/td[4]/text() | //tr[@class="bg-grayf7"]/td[4]/text()')
    print(companys)
    properties = selector.xpath('//tr[@class=""]/td[3]/a/text() | //tr[@class="bg-grayf7"]/td[3]/a/text()')
    print(properties)
    presellnumber=selector.xpath('//tr[@class=""]/td[2]/a/text() | //tr[@class="bg-grayf7"]/td[2]/a/text()')
    print(presellnumber)
    locations = selector.xpath('//tr[@class=""]/td[5]/text() | //tr[@class="bg-grayf7"]/td[5]/text()')
    print(locations)
    dates = selector.xpath('//tr[@class=""]/td[6]/text() | //tr[@class="bg-grayf7"]/td[6]/text()')
    print(dates)
    id_list = selector.xpath('//tr[@class=""]/td[3]/a/@href | //tr[@class="bg-grayf7"]/td[3]/a/@href')
    print(id_list)
    res = []
    for i in range(len(companys)):
        line = []
        line.append(companys[i].strip())
        line.append(properties[i].strip())
        line.append(presellnumber[i].strip())
        line.append(locations[i].strip())
        line.append(dates[i].strip())
        line.append("http://zjj.sz.gov.cn/ris/bol/szfdc/"+id_list[i].strip())

        newline = ','.join(line)
        res.append(newline)
    return res

outlines = []

for page in range(1):
    outlines += grab_page()
outline = '\n'.join(outlines)
with open("properties.csv", "w") as myfile:
    myfile.write(outline)
