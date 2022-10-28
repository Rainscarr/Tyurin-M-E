# -*- coding: utf-8 -*-

def a_ya (n):
    for i in n.split(' '):
        if i[0]=='а' or i[-1]=='я':
            print(i)

a_ya(str(input()))