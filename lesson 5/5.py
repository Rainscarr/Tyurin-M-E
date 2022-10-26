# -*- coding: utf-8 -*-

from re import S


def sequence ():
    p = 0
    while True:
        n = int(input())
        if n == 0:
            break
        else:
            p+=1
    print('Ответ: ',p)

sequence()