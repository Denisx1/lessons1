import random
number = int(input('Введите число '))
a = random.randint(0,100)
r = a
i = 1
while i <= 9:
    if number != a:
        number = int(input('Еще одна попытка '))
        i += 1
print('Вы не угадали ни разу но число случайное число = ' + str(r))  
















    # if number > a:
    #     print(number, ' больше а')
    #     number = int(input())
    # elif number < a:
    #     print(number, 'Меньше а')
    #     number = int(input())
    # else:
    