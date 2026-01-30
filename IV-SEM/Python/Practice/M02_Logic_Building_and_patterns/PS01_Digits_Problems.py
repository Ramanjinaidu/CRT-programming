#1 Count the number of digits in a given number.
"""
n = int(input())
print(len(str(n)))

or

n = int(input())
count = 0
for i in str(n):
    count += 1
print(count)
"""
#2 Finding sum of digits in a number
"""
n = int(input())
s = 0
for i in str(n):
    digit = n%10
    s += digit
    n = n//10
print(s)

# 3 Reverse the number
n = int(input())
rev = 0
while n>0:
    digit = n%10
    rev = rev*10 + digit
    n = n//10
print(rev)
"""
# 4 check palindrome number
"""
n = int(input())
rev = 0
temp = n
while n>0:
    digit = n%10
    rev = rev*10 + digit
    n = n//10
if rev == temp:
    print("Palindrome")
else:
    print("Not a palindrome")
"""
# 5 check Armstrong number
"""
n = int(input())
temp = n
s = 0
l = len(str(n))
for i in range(l):
    digit = n%10
    s += digit**l
    n = n//10
if s == temp:
    print("Armstrong Number")
else:
    print("Not an Armstrong number")
"""

#6 Find largest digit in a number
"""
n = int(input("Enter a number:"))
largest = 0
while n>0:
    digit = n%10
    n = n//10
    if digit > largest:
        largest = digit
print(largest)
"""
#7 Find the Smallest digit in a number
"""
n = int(input())
smallest = 9
while n>0:
    digit = n%10
    n //= 10
    if digit<smallest:
        smallest = digit
print(smallest)
"""

#8 count the number of zeros
"""
n = int(input())
zero_count = 0
while n> 0:
    digit = n%10
    n = n//10
    if digit == 0:
        zero_count += 1
print(zero_count)
"""
#9 Digital Sum problem
"""
n = int(input())
while n>10:
    s = 0
    while n>0:
        s += n%10
        n = n//10
    n = s
print("Digital Sum:",s)
"""
#10 Checking of SPY number

n = int(input())
s = 0
p = 1
while n>0:
    s += n%10
    p *= n%10
    n = n//10
if s == p:
    print("SPY number")
else:
    print("NOt a SPY number")