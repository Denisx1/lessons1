# n = int(input())
# x = 0
# y = 0
# while n != 0:
#     n = int(input())
#     y+=1
#     x+=1
# print(x / y)    
# n = 1
# x = []
# while n!=0:
#     n = int(input())
#     if n % 2 == 0:
#         x.append(n)
# print(x)
# print(len(x))
# n = 1
# c = 0
# while n!=0:
#     n = int(input())
#     if n %2 == 0:
#         c += 1
#         print(c)

# print(s.split())
# def split_pairs(a):
#     a = input()
    # # your code here
    # if len(a) % 2 == 0:
    # s = a[:((len(a)//2))] .ljust(2,a[1])     
    # w = a[((len(a)//2)) if len(a)%2 == 0
    # else (((len(a)//2))):].ljust(2, '_')
    # return a[:((len(a)//2))] .ljust(2,a[1]),a[((len(a)//2)) if len(a)%2 == 0
    #  
    #
    #                               else (((len(a)//2))+1):].ljust(2, '_')

    # for i in a:
    #     a[i] = i.split(',')
    # return [a]

    # else (((len(a)//2))):].ljust(2, '_')
    #print(list(map(''.join, zip(*[iter(a + '_')]*2))))
    #return (''.join, zip(a[::2]) if len(a) % 2 == 0 else a + '_')
    #return (list(map(''.join, zip(*[iter(a if len(a) % 2 == 0 else a + '_')]*2))))
    
      
#     a += '_' if len(a) % 2 != 0 else ''
#     return [a[i:i+2] for i in range(0, len(a), 2)] 
         

                                                
    
# print(split_pairs(123))

# if __name__ == '__main__':
#     print("Example:")
#     print(list(split_pairs('abcd')))

#     # These "asserts" are used for self-checking and not for an auto-testing
#     assert list(split_pairs('abcd')) == ['ab', 'cd']
#     assert list(split_pairs('abc')) == ['ab', 'c_']
#     assert list(split_pairs('abcdf')) == ['ab', 'cd', 'f_']
#     assert list(split_pairs('a')) == ['a_']
#     assert list(split_pairs('')) == []
#     print("Coding complete? Click 'Check' to earn cool rewards!")
# def beginning_zeros(s: str) -> int:
#     # your code here
#     str.index(/[^0]/) || str.length
#     # n.find(0, 1,) - 1
# n = input()
# print(beginning_zeros(n))
# if __name__ == '__main__':
#     print("Example:")
#     print(beginning_zeros('100'))

#     # These "asserts" are used for self-checking and not for an auto-testing
#     assert beginning_zeros('100') == 0
#     assert beginning_zeros('001') == 2
#     assert beginning_zeros('100100') == 0
#     assert beginning_zeros('001001') == 2
#     assert beginning_zeros('012345679') == 1
#     assert beginning_zeros('0000') == 4
#     print("Coding complete? Click 'Check' to earn cool rewards!"n = int(input())
# n = int(input())
# a = [['.']*n for i in range(n)]
# i = n//2
# for j in range(n):
#     a[i][j] = a[j][i] = '*'
# for i in range(n):
#     for j in range(n):
#         if i == j or i == (n-j-1):
#             a[i][j] = '*'    
# for i in a:
#     print(i)    
# num_zeroes = 0
# for i in range(int(input())):
#     if int(input()) == 0:
#         num_zeroes += 1
# print(num_zeroes)
# def beginning_zeros(number: str) -> int:
#     cnt = 0
#     for s in number:
#         if s != '0':
#             break
#         else:
#             cnt += 1
#     return cnt
# print(beginning_zeros(input()))   
# a, n, find_num = [int(i) for i in input().split()], int(input()), 100
# for i in range(len(a)):
#     if a[i] < n:
#         find_num = -find_num
#     else:
#         find_num = find_num + 0
#     if a[i] >= n and a[i] - n <= find_num - n:
#         find_num = a[i]
#     elif a[i] <= n and find_num - n <= a[i] - n:
#         find_num = a[i]
# print(find_num)
# def nearest_value(values: set, one: int) -> int:
#     return min(values, key=lambda n: (abs(one - n), n))
# print(nearest_value(int(input())))
# def correct_sentence(text: str) -> str:
#     if text[-1] != '.': 
#         return text.title() + '.'
#     else:
#         return text.title()  
# def cap(line):        
# #     return ' '.join(s[:1].upper() + s[1:] for s in line.split(' '))       
# # # print(correct_sentence('greetings, friends'))  
# # print(cap('Greetings, friends'))  
#     # return (True if line % 2 == 0 else False)
# print(cap(int(input())))    
# def split_list(items: list) -> list:
#     if len(items) %2 == 0:
#         return [items[:((len(items)//2)+1)]]   
#     else:
#         return [items[((len(items)//2)+2):]]
# print(split_list('1, 2, 3, 4, 5,'))    
# def split(alist, wanted_parts=2):
#     length = len(alist)
#     return [ alist[i*length // wanted_parts: (i+1)*length // wanted_parts]
#              for i in range(wanted_parts) ]
# A = [0,1,2,3,4,5,6,7,8]            
# print(split(A))             
# def split(arr, size):
#      arrs = []
#      while len(arr) > size:
#          pice = arr[:size]
#          arrs.append(pice)
#          arr   = arr[size:]
#      arrs.append(arr)
#      return arrs

# x=[1, 2, 3, 4, 5,]
# print(split(x, 5))   

# def sum_numbers(text: str) -> int:
#     return sum(int(i) for i in text.split() if i.isdigit())
# print(sum_numbers('This picture is an oil on canvas '
#  'painting by Danish artist Anna '
#  'Petersen between 1845 and 1910 year')) 
# def checkio(array: list) -> int:
    
        
    

   
# print(checkio([0, 1, 2, 3, 4, 5])) 
# def checkio(words: str) -> bool:
    # count = 0               
    # for i in words.split(): 
    #     if not i.isalpha():     
    #         count = 0       
    #     else:               
    #         count += 1      
    #     if count == 3:      
    #         return True     
    # return False
# print(checkio("Hello World hello")) 
# diction = dict(input().split() for i in range(int(input())))
# slovo = input()
# diction

# for key, val in diction.items():
#     if slovo == val:
#         print(key)
#     elif key == slovo:
#         print(val)    
# n = int(input())
# d = {}
# for i in range(n):
#     first, second = input().split()
#     d[first] = second
#     d[second] = first
# print(d[input()])

dict = {'iregular verbs':
    ['be', 'was were',	'been', '-', 'быть']
    ['beat', 'beat', 'beaten', '-',	'бить']
    []}
    12332423423423423423423
        