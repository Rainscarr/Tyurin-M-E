# # -*- coding: utf-8 -*-

def sequence (n):
    count = 0
    maxx = 0
    for i in n:
        if i == 'н':
            count +=1        
        else:
            if count>maxx:
                maxx=count
                count = 0
    print(max([maxx, count]))

sequence(input())








