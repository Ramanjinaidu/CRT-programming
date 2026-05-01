"""
# Bubble Sort

def BubbleSort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(n-1-i):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
    return arr
print(BubbleSort([5,1,4,2,3]))

# Selection Sort

def Selection_Sort(nums):
    n = len(nums)
    for i in range(n):
        pos = i
        for j in range(i+1,n):
            if nums[j] < nums[pos]:
                pos = j
        nums[i],nums[pos] = nums[pos],nums[i]
    return nums
print(Selection_Sort([5,1,4,2,3]))
"""
# Insertion Sort

def Insertion_Sort(nums):
    n = len(nums)
    for i in range(1,n):
        j = i-1
        key = nums[i]
        while j >= 0 and nums[j] > key:
            nums[j+1] = nums[j]
            j -= 1
        nums[j+1] = key
    return nums
print(Insertion_Sort([5,1,4,2,3]))