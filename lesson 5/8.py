# -*- coding: utf-8 -*-

def max_sequence ():
    max = p = 0
    first = int(input())
    while True:
        if first == 0:
            break
        second = int(input())
        if second==first:
            p+=1
            if p>max:
                max=p
        else:
            p=0
        first=second
    print('Ответ: ',max+1)

max_sequence()