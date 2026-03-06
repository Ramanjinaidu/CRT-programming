"""
a = int(input())
b = int(input())

print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b)
print(a**b)
print(a%b)

# Math buit-in Functions

print(abs(-50))
print(round(5.908))
print(min([10,20,30]))
print(max([10,20,30]))
print(sum([10,20,30]))
print(pow(2,3))

# Math module functions

import math
print(math.sqrt(81))
print(math.ceil(4.2))
print(math.floor(4.2))
print(math.pi)
print(math.factorial(5))

# GCD of a two numbers
import math
a = int(input())
b = int(input())
print(math.gcd(a,b))
"""
import math
a = int(input())
b = int(input())
gcd = math.gcd(a,b)
print((a*b)//gcd)