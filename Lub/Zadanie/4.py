n1 = int(input('First number '))
n2 = int(input('Second number '))
n3 = int(input('Third number '))
list = sorted([n1, n2, n3])
while True:
    if list[0] + list[1] != list[2]:
        print('No')   
        n1 = int(input('First number '))
        n2 = int(input('Second number '))
        n3 = int(input('Third number '))
        list = sorted([n1, n2, n3])
    else:
        list[0] + list[1] == list[2]
        print('Yes')    
        break    
