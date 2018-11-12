#!/usr/bin/python
# coding: utf-8

def main():
    flag = ""

    string = "Hobbangman Ilikeapeach Pooh&Piglet"
    arr = string.split(' ')

    for i in range(0, 6):
        # H + P - I
        c1 = arr[0][i]
        c2 = arr[1][i]
        c3 = arr[2][i]

        tmp = chr(ord(c1) + ord(c3) - ord(c2))
        flag += tmp

    string = "Pokemongo! Hobbangman Ilikeapeach Pooh&Piglet"
    arr = string.split(' ')

    for i in range(6, 10):
        # n - p + g
        c1 = arr[0][i]
        c2 = arr[1][i]
        c3 = arr[2][i]

        tmp = chr(ord(c1) - ord(c3) + ord(c2))
        flag += tmp

    print "[*] flag : %s (length : %d)" % (flag, len(flag))

if __name__ == '__main__':
    main()


