# -*- coding: utf-8 -*-

def odd (a,b):
    for i in range(a,b +1):
        if i % 2 != 0:
            print(i)

odd (int(input('Enter A: ')), int(input('Enter B: ')))