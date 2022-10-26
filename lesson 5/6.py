# -*- coding: utf-8 -*-


def average_value ():
    value = 0
    k = 0
    while True:
        n = int(input('n:'))
        if n == 0:
            break
        else:
            value+=n
            k+= 1
    print(value / k)

    

average_value()