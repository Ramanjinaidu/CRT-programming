# Triangle pattern
"""
n = int(input())
for i in range(1,n+1):
    for sp in range(n-i):
        print(" ",end = " ")
    for j in range(i*2-1):
        print("*",end = " ")
    print()
"""
# or
"""
n = int(input())
for i in range(1,n+1):
    print(" "*(n-i) + "* "*i)
"""
# Reverse Triangle
"""
n = int(input())
for i in range(n,0,-1):
    print(" "*(n-i)+"* "*i)
print()
"""

# Diamond pattern
"""
n = int(input())
for i in range(1,n+1):
    print(" "*(n-i) + "* "*i)
for i in range(n-1,0,-1):
    print(" "*(n-i)+"* "*i)
print()
"""
# Palindrome Pattern
"""
1
212
32123
4321234
"""
