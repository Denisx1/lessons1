fullName = input('Имя  (на Английском): ')
surname = input('Введите фамилию (in English) ')

name1 = 'Ivan'
name2 = 'Alexey'
surname1 = 'Ivanov'
surname2 = 'Vybodovsky'

if fullName == name1 or surname == surname1 and fullName == name2 or surname == surname2:
    print('Вы в розыске ')
else:
    print('Привет ')    
   