"""
# 1 Max Function
arr = [10,20,30,40]
print(max(arr))

# 2 Check palidrome using reversed() & join()
word = "madam"
if word == "".join(reversed(word)):
    print("Palindrome")
else:
    print("Not a Palindrome")

# 3 Filter Function count Even Numbers

arr = [10,23,24,54,85,10,25]
res = list(filter(lambda x:x%2==0,arr))
print(res)

# 4 Remove duplicates using set()
arr = [10,20,30,30,20,10]
A = set(arr)
print(A)

#5 Sum of digits of number using sum()
n = 123
digit_sum = sum(int(digit) for digit in str(n))
print(digit_sum)

#7 common elements using set()
a = set([10,25,48,9,7,8])
b = set([20,30,25,10,16,15])
print(a&b)
"""