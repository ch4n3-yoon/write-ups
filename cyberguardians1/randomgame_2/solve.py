#!/usr/bin/python
# coding: utf-8

from pwn import *
from ctypes import *
import random

p = remote('52.78.156.241', 4885)

def menu(choice):
    c = str(choice)
    p.recvuntil('User : ')
    p.sendline(c)

    res = p.recvline()
    print res

    if res.find('lose!') > -1:
        return choice
    elif res.find('Draw!') > -1:
        choice = choice + 1
        return choice % 3
    else:
        choice = choice - 1
        if choice == 0:
            return 3
        else:
            return choice


choices = [1,1,1,1,1,1,1,1,1,1,2]
for i in range(10):
    # menu(random.randint(1,4))
    choices[i] = menu(choices[i])

p = remote('52.78.156.241', 4885)

for c in choices:
    menu(c)

p.interactive()
