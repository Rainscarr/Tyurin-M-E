# -*- coding: utf-8 -*-

def chocolate (n,m,k):
    if ((k%n==0) or (k%m == 0)) and (k < n*m):
        print('Да')
    else:
        print('Нет')

chocolate(int(input('Enter n: ')),int(input('Enter m: ')),int(input('Enter k: ')),)