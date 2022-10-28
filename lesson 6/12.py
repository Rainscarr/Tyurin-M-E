# -*- coding: utf-8 -*-

def seq_len (n):
    for i in n.split(' '):
        if i[-1] == 'я':
            print(i)
seq_len(str(input()))