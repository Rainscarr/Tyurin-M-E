# -*- coding: utf-8 -*-

def delete_a (n):
    rep = 0
    for i in n:
        if i== 'a':
            rep +=1
    print(n.replace('a',''),'Удаления:', rep)
    
delete_a(str(input()))