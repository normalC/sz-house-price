import json
from lxml import etree
import urllib.request
from urllib import parse
import re
import time

from urllib.parse import quote
import string




url = "http://zjj.sz.gov.cn/ris/bol/szfdc/index.aspx"
print(url)
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.75 Safari/537.36'}
req = urllib.request.Request(url=url, headers=headers)
response = urllib.request.urlopen(req)
result = response.read().decode('utf-8')
selector = etree.HTML(result, parser=None, base_url=None)
print(selector)

VIEWSTATE = re.findall(r'<input type="hidden" name="__VIEWSTATE" id="__VIEWSTATE" value="(.*?)" />', result, re.I)
EVENTVALIDATION = re.findall(r'input type="hidden" name="__EVENTVALIDATION" id="__EVENTVALIDATION" value="(.*?)" />',result, re.I)

VIEWSTATE=VIEWSTATE[0]
EVENTVALIDATION=EVENTVALIDATION[0]
page=2
'print(VIEWSTATE)'
'print(EVENTVALIDATION)'

''''scriptManager2':'updatepanel2|AspNetPager1','''
postdata =urllib.parse.urlencode( {
'scriptManager2':'updatepanel2|AspNetPager1',
'__EVENTTARGET':'AspNetPager1',
'__EVENTARGUMENT':page,
'__LASTFOCUS':'',
'__VIEWSTATE':VIEWSTATE,
'__VIEWSTATEGENERATOR':'2A35A6B2',
'__VIEWSTATEENCRYPTED':'',
'__EVENTVALIDATION':EVENTVALIDATION,
'tep_name':'',
'organ_name':'',
'site_address':'',
'ddlPageCount':'10',
},doseq=True)
type(postdata)
print(postdata)

req = urllib.request.urlopen(url = url,data =postdata)


"https://blog.51cto.com/slliang/1783837"

companys = selector.xpath('//tr[@class="tab_body bd0"]/td[1]/text() | //tr[@class="tab_body bd1"]/td[1]/text()')
properties = selector.xpath('//tr[@class="tab_body bd0"]/td[2]/text() | //tr[@class="tab_body bd1"]/td[2]/text()')
locations = selector.xpath('//tr[@class="tab_body bd0"]/td[3]/text() | //tr[@class="tab_body bd1"]/td[3]/text()')
districts = selector.xpath('//tr[@class="tab_body bd0"]/td[4]/text() | //tr[@class="tab_body bd1"]/td[4]/text()')
id_list = selector.xpath('//tr[@class="tab_body bd0"]/td[5]/a/@val | //tr[@class="tab_body bd1"]/td[5]/a/@val')
res = []
for i in range(len(companys)):
    line = []
    line.append(companys[i])
    line.append(properties[i])
    line.append(locations[i])
    line.append(districts[i])
    line.append(id_list[i])
    newline = ','.join(line)
    res.append(newline)


