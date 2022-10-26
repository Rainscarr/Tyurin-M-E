# -*- coding: utf-8 -*-

def max_power(n):
    a = 0
    f = 1
    while f*2<=n:
        f*=2
        a+=1
    print('Показатель:',f,'Степень:',a)

max_power(int(input('n: ')))