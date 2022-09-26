def more_than_five(lst):
    new_lst = []
    for number in lst:
        if abs(number) > 5:
            new_lst.append(number)
    
more_than_five([1,2,3,4,5,6,7,7,3])