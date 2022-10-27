# -*- coding: utf-8 -*-

def replace_p (n):
    x = n[:len(n)//2]
    print(x.replace('п','*'),end ='')
    print(n[len(n)//2: ])
    
replace_p(str(input()))