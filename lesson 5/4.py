# -*- coding: utf-8 -*-

def run (x):
    y = int(input('y:'))
    day = 1
    while y-x > 0:
        x =x+(x/100*10)
        day += 1
    print(day)

run(int(input('x: ')))