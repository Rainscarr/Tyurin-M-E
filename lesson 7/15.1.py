# -*- coding: utf-8 -*-

def lst (lst):
    lst.split()
    non_unique = [i for i in set(lst) if lst.count(i) > 1]
    print(non_unique)

lst(input())

