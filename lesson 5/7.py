# -*- coding: utf-8 -*-

def sequence ():
    p = 0
    first = int(input())
    while True:
        if first == 0:
            break
        second = int(input())
        if second>first:
            p+=1
        first=second
    print('Ответ: ',p)

sequence()