print("Как тебя зовут?")
name = input()
print('Привет',name + '!', 'Твой первый вопрос!')
q1 = input('Пожар китаец?  \n 1. Да \n 2. Нет \n 3. Незнаю \n' )


if q1 == '1' or q1 == 'Да':
    true1 = 'Ответ верный!'
    print(true1)
else: 
    false1 = 'Неверно'
    print(false1)

print('Второй вопрос: ')

q2 = input(f'Сколько букв в твоем имени? \n 1. 7 \n 2. {len(name)} \n 3. Незнаю \n 4. 9 \n' )

if q2 == '2' or q2 == str(len(name)):
    true2 = 'Ответ верный!'
    print(true2)
else: 
    false2 = 'Неверно'
    print(false2)

print('Третий вопрос: ')

q3 = input('Достается ли еда Михе в обед? \n 1. Да \n 2. Нет \n 3. Незнаю  \n')

if q3 == 'нет' or q3 == '2':
    true3 = 'Ответ верный!'
    print(true3)
else: 
    false3 = 'Неверно'
    print(false3)

print('Четвертый вопрос: ')

q4 = input('Куда отправится Олександр если провалит собеседование в Hebron-e? \n 1. На завод \n 2. Буткемп к Navi \n 3. Поедет домой  \n 4. Незнаю \n')

if q4 == '1' or q4 == 'На завод':
    true4 = 'Ответ верный!'
    print(true4)
else: 
    false4 = 'Неверно'
    print(false4)

q5 = input('Как поднять ПТС-Ы в доте2?  \n 1. Никак \n 2. Больше играть \n 3. Удалить доту  \n 4. Учится играть \n')

if q5 == 'Удалить доту' or q5 == '3':
    true5 = 'Ответ верный!'
    print(true5)
else: 
    false5 = 'Неверно'
    print(false5)


