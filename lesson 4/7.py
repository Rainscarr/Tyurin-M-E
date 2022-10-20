# -*- coding: utf-8 -*-

def sum_fact():
    n = int(input('n: '))
    factorial = 1
    fact_sum = 0
    for i in range(1, n + 1):
        factorial *= i
        fact_sum += factorial
    print(fact_sum)

sum_fact()