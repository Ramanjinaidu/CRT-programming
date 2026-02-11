#1. Print Square pattern
"""
n = int(input())
for i in range(n):
    for j in range(n):
        print("*",end = " ")
    print()
"""
#2. Right Angle Triangle
"""
n = int(input())
for i in range(n):
    for j in range(i+1):
        print("*",end = " ")
    print()
"""
#3. Inverted Triangle
"""
n = int(input())
for i in range(n):
    for j in range(n-i):
        print("*",end = " ")
    print()
"""
#4. Number Triangle
"""
n = int(input())
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end = " ")
    print()
"""
#5. Repeated Number Pattern
"""
n = int(input())
for i in range(1,n+1):
    for j in range(1,i+1):
        print(i,end = " ")
    print()
"""
#6. Alphabet Triangle
"""
n = int(input())

for i in range(n):
    ch = 65
    for j in range(i+1):
        print(chr(ch+j),end = " ")
    print()
"""
#7. Floyd Triangle







#8. Hollow Square

n = int(input())
for i in range(n):
    for j in range(n):
        if i==0 or  i== n-1 or j == 0 or j == n-1:
            print("*",end = " ")
        else:
            print(" ",end = " ")
    print() 