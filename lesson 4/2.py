# -*- coding: utf-8 -*-
def F (A,B):
    if A<B:
        for i in range(A,B +1):
            print(i)
    else:
        for i in range(A,B -1, -1):
            print(i)
F(int(input('Enter a number: ')), int(input('Enter a number: ')))