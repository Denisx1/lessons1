number = int(input())
number2 = int(input())
number3 = int(input())
number4 = int(input())
x = []
y = []

if number % 2 != 0:
    x.append(number)
else:
    y.append(number)

if number2 % 2 != 0:
    x.append(number2)
else:
    y.append(number2)

if number3 % 2 != 0:
    x.append(number3)
else:
    y.append(number3)

if number4 % 2 != 0:
    x.append(number4)
else:
    y.append(number4)    
print('Непарные: ', sorted(x))
print('Парные: ', sorted(y))

    
    
