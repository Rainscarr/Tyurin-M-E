# -*- coding: utf-8 -*-

def palindrom (n):
    lst = set()
    for i in range(1,n+1):
        for j in range(2,i):
            if i%j == 0:
                break
            else:
                bin_i = bin(i)[2:]
                if ''.join(reversed(bin_i)) == bin_i:
                    lst.add(bin_i)
    lst = sorted(list(map(lambda n: int(n, 2), lst)))
    for n in lst:
        print(n)             


palindrom(int(input('n: ')))