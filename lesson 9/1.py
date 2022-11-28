# -*- coding: utf-8 -*-

c = 0
s = 0
n = 3
A = []
for i in range (n):
    b=[]
    for j in range (n):
        print('Enter [', i,' ,', j,'] element')
        b.append(int(input()))
    A.append(b)

for i in range (n):
    for j in range (n):
        print("%2d " % A[i][j], end='')
    print()

for i in range(n):
    for j in range(i + 1, n):
        if A[i][j] > 0:
            s += A[i][j]
            c += 1
print("Кол-во:",c)
print("Sum:",s)




