# -*- coding: utf-8 -*-

def summ_numbers(n):
    if n <= 0:
        return n

    return n % 10 + summ_numbers(n // 10)


def main():
    n = int(input('N: '))

    print(summ_numbers(n))


main()