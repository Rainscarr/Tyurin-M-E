# -*- coding: utf-8 -*-

def sum_n ():
    n = int(input())
    s=0
    for i in range(1, n+1):
        s += i**3
    print(s)

sum_n()