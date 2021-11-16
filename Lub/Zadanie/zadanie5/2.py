list = ['The history book', 'The military', 'Arms', 'Arms & Armour', 
        'Gmat', 'Gmat review', 'Test study', 'Exam success', 'Murder on the Orient',
        'The Great Gutsby', 'Short stories']

def all_eq(lst):
    big_element = max(lst, key = len)
    maximum = len(big_element)
    iter = 0
    for i in lst:
        lst[iter] = i.ljust(maximum, '_')
        iter += 1 
    return lst
list = all_eq(list)
for i in list:
    print(i)