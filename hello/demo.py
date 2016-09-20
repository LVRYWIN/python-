#!/usr/bin/python
#coding=utf-8
##查询天气的demo
import urllib2
import json
from hello.city import city
cityname = raw_input('你想查哪个城市的天气?\n')
citycode = city.get(cityname)
if citycode:
    url = ('http://www.weather.com.cn/data/cityinfo/%s.html'% citycode)
    content = urllib2.urlopen(url).read()
    data = json.loads(content)
    result = data['weatherinfo']
    for k in result:
        print ('%s : %s ')%(k,result[k])
    print content
else:
    print '你输入的城市有误'
