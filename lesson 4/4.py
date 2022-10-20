# -*- coding: utf-8 -*-

def sum_N (N):
    n = 0
    for i in range(N):
        n += int(input())
    print('Sum: ',n)
sum_N(int(input('N: ')))