n = int(input())
s = 0
m = 1

while n > 0:
    i = n % 10
    s += i
    m *= i
    n //= 10
print(s)
print(m)    
