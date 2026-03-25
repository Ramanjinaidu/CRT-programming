"""
#1 Reverse the array Elements
arr = [1,2,3,4,5]
print(arr[::-1])
# Using reverse method
arr.reverse()
print(arr)
# Check if an array is sorted or not

arr = [1,2,3,4,5,3,5,2]
print(max(arr))
print(min(arr))
A = set(arr)
print(A)
"""
# Frequency of the array
a = [10,20,30,40,50,50,40,30,20,10]
d = {}
for i in a:
    d[i] = d(i,0) + 1
print(d)