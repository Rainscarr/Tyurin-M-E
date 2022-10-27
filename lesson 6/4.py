# -*- coding: utf-8 -*-

def replace_a (n):
    rep = 0
    for i in n:
        if i == 'a':
            rep+=1
    print(n.replace('a','o'))
    print('Кол-во замен: ',rep)
    print('Символов в строке: ',len(n))

replace_a(str(input('Enter a string: ')))