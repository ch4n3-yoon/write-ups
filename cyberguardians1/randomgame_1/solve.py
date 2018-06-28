#!/usr/bin/python
# coding: utf-8

from pwn import *
from ctypes import *
import random

p = remote('52.79.210.195', 9292)

def menu(choice):
    c = str(choice)
    p.recvuntil('User : ')
    p.sendline(c)

    res = p.recvline()

    if res.find('Draw!') > -1:
        choice = choice -1
        if choice == 0:
            choice = 3
        return choice

    elif res.find('lose!') > -1:
        choice = choice + 1
        if choice == 4:
            choice = 1
        return choice

    else:
        return choice


choices = [1,2,3,3,1,3,3,2,3,3]
for i in range(10):
    # menu(random.randint(1,4))
    choices[i] = menu(choices[i])

p = remote('52.79.210.195', 9292)

for c in choices:
    menu(c)

p.interactive()
