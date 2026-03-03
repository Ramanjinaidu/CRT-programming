# Lists
"""
It is represented as []
it is mutable
built-in methods:
append()
insert()
extend()
pop()
remove()
clear()
sort(),sort(reverse = True)
rverse()
index() return index
count()
copy()
max()
min()
len()
list()
sorted()
reversed()
"""

# Leet code Questions
#1480
"""
li = list(map(int,input().split()))
li1 = []
total = 0
for i in li:
    total += i
    li1.append(total)
print(li1)
    or
li = [1,2,3,4]
res = []
for i in range(1,len(li)+1):
    res.append(sum(li[:i]))
print(res)
"""
#217
"""
nums = [1,2,3]
if nums == list(set(nums)):
    print(False)
else:
    print(True)
"""
#1672
"""
accounts = [[1,2,3],
            [3,2,1]]
max_wealth = sum(accounts[0])
for i in range(len(accounts)):
    if sum(accounts[i]) > max_wealth:
        max_wealth = sum(accounts[i])
print(max_wealth)
"""
#268
"""
arr = list(map(int,input().split()))
n = len(arr)
sum_n = (n*(n+1))//2
sum_arr = 0
for i in range(n):
    sum_arr += arr[i]
print(sum_n-sum_arr)
"""
