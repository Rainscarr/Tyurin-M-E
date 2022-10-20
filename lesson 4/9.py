# -*- coding: utf-8 -*-

def fibonacci (n):
    summa = 2
    f1 = 1
    f2 = 1
    while n > 2:
        f1,f2 = f2,f1+f2
        summa += f2
        n -= 1
    print()
    print('Сумма = ', summa)

fibonacci(int(input('n: ')))

