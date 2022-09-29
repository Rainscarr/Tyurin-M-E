# -*- coding: utf-8 -*-

def leap_year (number):
    if (number % 4 == 0) and (number % 100 != 0) or (number % 400 == 0):
        print('Да')
    else:
        print('Нет')
leap_year(int(input('Enter a number: ')))
