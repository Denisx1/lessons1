a = int(input('First ')) 
b = int(input('Second '))
while max(a, b) % min(a, b) != 0:
    if a > b:
        a = a % b
    elif a < b:
        b = b % a
print ('Result ' + str(min(a,b)))