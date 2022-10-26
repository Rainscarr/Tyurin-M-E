# -*- coding: utf-8 -*-

def dell (n):
    if n>= 2:
        for i in range(2, n+1):
            if n%i == 0:
                print(i)
                break
dell(int(input('n: ')))