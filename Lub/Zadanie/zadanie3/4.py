import random
number = int(input('Введите число от 0 до 100\n'))
a = random.randint(0,100)
i = 1
while i <= 9:
    if number != a:
        if number > a:
            print(number, 'это число больше рандомного')
        elif number < a:
            print(number, 'это число меньше рандомного')    
        number = int(input('Еще одна попытка '))
        i += 1
    else:
        print('Krasava')  
        break  
print('Вы не угадали ни разу но число случайное число = ' + str(a))  