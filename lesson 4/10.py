# -*- coding: utf-8 -*-

def fibonacci (k,n):
    summa = 0
    f1 = 1
    f2 = 1
    for i in range(3, n + k):
        f1, f2 = f2, f1 + f2
        if i >= k:
            summa += f2
    print('Сумма = ', summa)

fibonacci(int(input('k: ')), int(input('n: ')))