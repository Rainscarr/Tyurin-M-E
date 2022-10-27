# -*- coding: utf-8 -*-

def replacee (n):
    rep = 0
    for i in n:
        if i == '.':
            rep+=1
    print(n.replace('.',''),'Кол-во удалений: ',rep)

replacee(str(input('Enter a string: ')))