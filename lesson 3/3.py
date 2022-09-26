# -*- coding: utf-8 -*-
from math import floor 
def time (n):
    n = n % (60 * 24)
    hours = floor(n/60)
    n = floor(n%60) 
    print(f'{str(hours).zfill(2)}:{str(n).zfill(2)}') 
time(int(input('enter a minutes: ' )))