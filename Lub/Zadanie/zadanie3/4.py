import random
number = int(input('Введите число от 0 до 100 \n'))
a = random.randint(0,100)
i = 1
while i <= 9:
    if number != a:
        number = int(input('Еще одна попытка\n'))
        i += 1
    else:
        print('Krasava')    
print('Вы не угадали ни разу но число случайное число = ' + str(a))  