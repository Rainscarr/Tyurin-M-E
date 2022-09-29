# -*- coding: utf-8 -*-

def same_color (a,b,c,d):
    e = (a + b) % 2
    f = (c + d) % 2
    if e == f:
        print('ДА!')
    else:
        print('Нет!')
same_color(int(input()),int(input()),int(input()),int(input()))