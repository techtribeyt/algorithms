def insert_sort1(lst): 
    for i in range(1, len(lst)): 
        key = lst[i] 
        j = i - 1
        while j >=0 and key < lst[j] : 
                lst[j + 1] = lst[j] 
                j -= 1
        lst[j + 1] = key 
    return lst



def insert_sort2(lst):
    for i in range(1, len(lst)):
        j = i
        while j > 0 and lst[j - 1] > lst[j]:
            lst[j - 1], lst[j] = lst[j], lst[j - 1]
            j -= 1
    return lst

# import random
# insert_sort1(random.sample(range(1, 20), 10))
