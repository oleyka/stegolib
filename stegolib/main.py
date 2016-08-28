#!/usr/bin/env python


def rotN(n, cipher):
    if abs(n) > 25:
        raise ValueError

    res = ''

    for i in range(len(cipher)):
        res += chr(ord(cipher[i]) + n)

    return res
