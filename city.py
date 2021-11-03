import json
from typing import List

from lxml import etree
import urllib.request
from urllib import parse
import re
import time

def get_hiddenvalue(url):
    request=urllib.request.Request(url)
    reponse=urllib.request.urlopen(request)
    resu=reponse.read().decode("utf-8")
    VIEWSTATE =re.findall(r'<input type="hidden" name="__VIEWSTATE" id="__VIEWSTATE" value="(.*?)" />', resu,re.I)
    EVENTVALIDATION =re.findall(r'input type="hidden" name="__EVENTVALIDATION" id="__EVENTVALIDATION" value="(.*?)" />', resu,re.I)
    return VIEWSTATE[0],EVENTVALIDATION[0]



def grab_page(pagesum):
    url = "http://zjj.sz.gov.cn/ris/bol/szfdc/index.aspx"
    #print(url)
    headers = {    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.75 Safari/537.36',
                   'Content-Type':'application/x-www-form-urlencoded'}
    #req = urllib.request.Request(url=url, headers=headers)
    #response = urllib.request.urlopen(req)
    #result = response.read().decode('utf-8')
    #selector = etree.HTML(result, parser=None, base_url=None)
    #print(selector)
    ressum=[]
    for page in range(1,pagesum):
        VIEWSTATE, EVENTVALIDATION=get_hiddenvalue(url)
        postdata =urllib.parse.urlencode(
            dict(scriptManager2='updatepanel2|AspNetPager1', __EVENTTARGET='AspNetPager1', __EVENTARGUMENT=page,
                 __LASTFOCUS='', __VIEWSTATE=VIEWSTATE, __VIEWSTATEGENERATOR='2A35A6B2', __VIEWSTATEENCRYPTED='',
                 __EVENTVALIDATION=EVENTVALIDATION, tep_name='', organ_name='', site_address='', ddlPageCount='10')).encode("utf-8")
        req = urllib.request.Request(url, data=postdata, headers=headers)

        # response = urllib.request.urlopen(req)
        # result = response.read().decode('utf-8')
        # selector = etree.HTML(result, parser=None, base_url=None)

        result=urllib.request.urlopen(req).read().decode("utf-8")
        selector = etree.HTML(result, parser=None, base_url=None)
        companys = selector.xpath('//tr[@class=""]/td[4]/text() | //tr[@class="bg-grayf7"]/td[4]/text()')
        properties = selector.xpath('//tr[@class=""]/td[3]/a/text() | //tr[@class="bg-grayf7"]/td[3]/a/text()')
        presellnumber = selector.xpath('//tr[@class=""]/td[2]/a/text() | //tr[@class="bg-grayf7"]/td[2]/a/text()')
        locations = selector.xpath('//tr[@class=""]/td[5]/text() | //tr[@class="bg-grayf7"]/td[5]/text()')
        dates = selector.xpath('//tr[@class=""]/td[6]/text() | //tr[@class="bg-grayf7"]/td[6]/text()')
        id_list = selector.xpath('//tr[@class=""]/td[3]/a/@href | //tr[@class="bg-grayf7"]/td[3]/a/@href')
        res=[]
        for i in range(len(companys)):
            line = []
            line.append(companys[i].strip())
            line.append(properties[i].strip())
            line.append(presellnumber[i].strip())
            line.append(locations[i].strip())
            line.append(dates[i].strip())
            line.append(id_list[i].strip())
            newline = ','.join(line)
            res.append(newline)
            res.append('\n')
            ressum.append(res)
            res = []
    #print(ressum)
    return ressum

outlines = []
outline= []
output=[]
outlines = grab_page(5)
rowNum = len(outlines)
columnNum = len(outlines[0])
print(rowNum,columnNum)
with open("properties.csv", "w") as myfile:
    myfile.write('')
#z整个深圳的预售
for i in range(0,rowNum):
    output= ''.join(outlines[i])
    with open("shenzhencity.csv", "a") as myfile:
        myfile.write(output)


