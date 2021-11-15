number = [1, 3, 6, 10, 12, 23, 10,
          2, 5, 8, 25, 21, 544, 123,
          87, 98, 32, 234, 231, 988,
          1014, 97, 65, 75, 85, 934,
          1098, 43, 29
        ]
def change(lst):
    number.sort()
    number[-1], number[0] = number[0], number[-1]
    return number
print(change(number))

   



