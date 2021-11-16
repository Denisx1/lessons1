list = [1, 3, 6, 10, 12,
          23, 10, 102, 23, 123,
          542, 231, 213, 121, 321,
           4, 5, 6, 654, 3451, 54
           ]
def to_dict(lst):
    iter = 0
    for i in lst: 
        lst[iter] = {i:i}
        iter += 1
    return lst
print(to_dict(list))

