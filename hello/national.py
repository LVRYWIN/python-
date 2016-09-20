#!/usr/bin/python
#coding=utf-8
##查询全国的
import urllib2
import json
##全部省份
url1 = 'http://m.weather.com.cn/data5/city.xml'
content1 = urllib2.urlopen(url1).read()
provinces = content1.split(',')
print content1
for i in provinces:
    print i


##全部城市
url = 'http://m.weather.com.cn/data3/city%s.xml'
for p in provinces[:3]:
    print '%s:\n\n'%p
    p_code = p.split('|')[1]
    url2 = url % p_code
    content2 = urllib2.urlopen(url2).read()
    print content2
    cities = content2.split(',')


