# -*- coding: utf-8 -*-

def stairs(n):
    if n <= 9:
        for i in range(1, n + 1):
            for a in range(1, i + 1):
                print(a, end='')
            print()

stairs(int(input()))