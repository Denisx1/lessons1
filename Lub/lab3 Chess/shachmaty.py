figure = input('Тип первую букву фигуры по английски (с большой буквы) ')
x1,y1 = int(input('Начальные координаты:\n' )), int(input())
#y1 = int(input())
x2,y2 = int(input('Конечные координаты:\n')), int(input())
#y2 = int(input())

def Chess(unit):
    if unit == 'P': #пешка 
        return abs(y1 - y2) <= 1 and x1 == x2

    elif unit == 'K': #Король
        return -1 <= x1 - x2 <= 1 and -1 <= y1 - y2 <= 1

    elif unit == 'T': #Тура
        return x1 == x2 or y1 == y2  

    elif unit == 'E': #Офицер
        return  abs(x1 - x2) == abs(y1 - y2) 

    elif unit == 'H': #Конь
        return 1 <= abs(x1 - x2) <= 2  and 1 <= abs(y1 - y2) <= 2

    elif unit == 'Q': #Ферзь
        return abs(x1 - x2) == abs(y1 - y2) or x1 == x2 or y1 == y2   

    raise ValueError('Неопределенный юнит : {}'.format(unit))
#Chess(figure)
print(Chess(figure))


# def checkerboard(n):
#     board = []
#     for vertical in range(4):
#         board.append([])
#         for horizontal in range(n):
#             board[vertical].append((vertical+horizontal) % 2)
#     return board

# for row in checkerboard(8):
#     print(row)
