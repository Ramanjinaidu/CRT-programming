"""
# implement Lower Bound 
# Linear Search

def Lower_Bound(arr,target):
    n = len(arr)
    for i in range(n):
        if arr[i] >= target:
            return i
    return n

print(Lower_Bound([10,20,30,40,50],30))
"""
# Binary Search
def Lower_bound(arr,target):
    low,high = 0,len(arr) - 1
    while low <= high:
        mid = (low + high)//2
        if target <= arr[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return low
print(Lower_bound([2,3,7,10,11,11,25],9))
print(Lower_bound([2,3,7,10,11,11,25],11))
print(Lower_bound([2,3,7,10,11,11,25],100))