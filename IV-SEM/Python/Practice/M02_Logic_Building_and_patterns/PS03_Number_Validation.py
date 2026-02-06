"""
1. Write a python code for the factorial of a given number?

n = int(input())
fact = 1
for i in range(1,n+1):
    fact *= i
print(fact)
"""
"""
2. Write a python code to check a number is armstrong number or not?

n = int(input())
temp = n
l = len(str(n))
s = 0
while n>0:
    digit = n%10
    s += digit**l
    n = n//10
if s == temp:
    print("Armstrong Number")
else:
    print("Not an Armstrong number")
"""

"""
3.Write a python code to check a number is prime number or not?

n = int(input("Enter a Number: "))
factors = 0
for i in range(1,n+1):
    if n%i == 0:
        factors += 1
if factors <= 2:
    print("Prime")
else:
    print("Not a Prime")
"""

"""
4. Print the prime numbers with in the Range?

start = int(input("Enter starting Value: "))
End = int(input("Enter End Value: "))
for num in range(start,End + 1):
    if num > 1:
        count = 0
        for i in range(1,num + 1):
            if num % i == 0:
                count += 1
        if count == 2:
            print(num,end = ' ')
"""

"""
5. Print the monotonic array

arr = list(map(int,input().split()))
Sorted_array = []

Sorted_array = arr.copy()
Sorted_array.sort()
Sorted_array.sort(reverse=True)

if arr == Sorted_array:
    print("Monotonic")
else:
    print("NOt a monotonic")
"""

"""
6.Revere Integer

n = int(input("Enter a Number: "))
sign = 1
if n<0:
    sign = -1
    n = -n
rev = 0
while n>0:
    digit = n%10
    rev = rev*10 + digit
    n = n//10
rev = rev * sign

if rev < -2**31 or rev > 2**31 -1:
    print(0)
else:
    print("Reversed Integer:",rev)
"""

"""
7. Happy NUmber
"""
n = int(input())
while n>0:
    s = 0
    digit = n%10
    s += digit**2
    n = n//10
if s == 1:
    print("Happy Number")
else:
    print("NOt a Happy Number")