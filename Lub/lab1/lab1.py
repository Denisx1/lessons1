what = input('Что делаем?? (+, -, %, /, *)\n')

number = int(input('Первое число '))
number1 = int(input('Второе число '))

if what == '+':
    res = number + number1
elif what == '-':
    res = number - number1
elif what == '*':
    res = number * number1
elif what == '%':
    res = number % number1
elif what == '/':
    res = number / number1                

print('Результат: ' + str(res))