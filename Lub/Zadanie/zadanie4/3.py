j = int(input('Сколько чисел нужно поместить в список(Введите число )'))
x = []
def to_list():
    y = 1
    while y <= j:
        n = int(input())
        x.append(n)
        y += 1
    return sorted(x)
print(to_list())        
             