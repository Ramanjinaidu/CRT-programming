# 1 print n natural numbers
# n = int(input())
# for i in range(1, n+1):
#     print(i,end = ' ')

# 2 print n even numbers
# n = int(input())
# for i in range(2,n+1,2):
#     print(i,end = ' ')

# 3 print n odd numbers
# n = int(input())
# for i in range(1,n+1,2):
#     print(i,end = ' ')

# 4 print finocci series
"""
n = int(input())
a = 0
b = 1
for i in range(n):
    print(a,end = ' ')
    c = a+b
    a,b = b,c
"""
# 5 print multiplication table of a number
""""
n = int(input())
for i in range(1,11):
    print(n,"x",i,"=",n*i)
"""
# 6 print the square of n natural numbers
"""
n = int(input())
for i in range(1,n+1):
    print(i**2,end=" ")
"""
# 7 print the cubes of the n natural numbers
"""
n = int(input())
for i in range(1,n+1):
    print(i**3,end=" ")
"""
# 8 print alternative series
"""
n = int(input())
for i in range(1,n+1):
    if i%2 == 0:
        print(-i,end = " ")
    else:
        print(i,end = " ")
"""
# 9 print the series 1,2,4,7,11,16,22
"""
n = int(input())
num = 1
print(num,end = " ")
for i in range(1,n):
    num += i
    print(num,end = " ")
"""
# 10 print the series 1,2,6,24,120
n = int(input())
num = 1
for i in range(1,n):
    num *= i
    print(num,end = ' ')