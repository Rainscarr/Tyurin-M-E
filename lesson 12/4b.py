# -*- coding: utf-8 -*-

def number(n, dell = 2):
    if n <= 2 or dell ** 2 > n:
        return True

    if n % dell == 0:
        return False

    return number(n, dell = dell + 1)


def number_n(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True


def main():
    print('YES' if number(int(input('N: '))) else 'NO')


main()