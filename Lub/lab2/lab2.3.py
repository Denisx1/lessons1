numb = int(input('Двузначное число: '))
print("Результат:")
for i in range(numb -1, 1, -1):
    if (numb % i == 0):
        print(i)
