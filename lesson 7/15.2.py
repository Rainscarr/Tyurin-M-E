# -*- coding: utf-8 -*-

import random
def lst ():
    lst = [random.randint(0, 10) for _ in range(10)]
    print(lst)
    res = []
    for i in lst:
        if i % 2 != 0:
            res.append(i)
    if len(res) == 0:
        print('No odd numbers')
 
    print(sorted(res, reverse=True))

lst()

 
