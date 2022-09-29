# -*- coding: utf-8 -*-

def same_numbers (a,b,c):
    if (a == b) and (a == c) and (b == c):
        print('3')
    elif (a == b) or (a == c) or (b == c):
        print('2')
    else:
        print('0')

same_numbers(int(input('Enter 1 number: ')),int(input('Enter 2 number: ')),int(input('Enter 3 number: ')))