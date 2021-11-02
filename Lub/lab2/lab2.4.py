number = int(input())
number2 = int(input())
number3 = int(input())

if number == number2 == number3:
    print('1')
elif number == number2 or number2 == number3 or number == number3:
    print('2')
else:
    print('3')    
    