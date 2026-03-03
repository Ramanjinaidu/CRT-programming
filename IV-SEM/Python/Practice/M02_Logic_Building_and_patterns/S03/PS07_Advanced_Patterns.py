#1 number triangle
"""
n = int(input())
for i in range(n):
    num = 1
    for j in range(i+1):
        print(num,end = " ")
        num = num * (i-j)//(j+1)
    print()
"""

#2.Butterfly problem

n = int(input())
for i in range(n):
    for j in range(i+1):
        print("*",end = " ")
    for sp in range(n-i-1):
        print(" ",end = " ")
    for sp in range(n-i-1):
        print(" ",end = " ")
    for j in range(i+1):
        print("*",end = " ")
    print()
for i in range(n):
    for j in range(n-i):
        print("*",end = " ")
    for sp in range(i):
        print(" ",end = " ")
    for sp in range(i):
        print(" ",end = " ")
    for j in range(n-i):
        print("*",end = " ")
    print()