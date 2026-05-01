"""
1.Linear Search(sequential search)
Time Complexity:
    Best Case ==> O(1)
    Average Case ==> O(n)
    Worst Case ==> O(n)
2.Binary search(Interval search) 
Time Complexity:
    Best Case ==> O(1)

def Linear_Search(nums,target):
    for i in range(len(nums)):
        if nums[i] == target:
            return i
        
    return -1
li = list(map(int,input().split()))
target = int(input())
print(Linear_Search(li,target))
"""

def Binary_Search(li,target):
    li.sort()
    low = 0
    high = len(li) - 1
    while low <= high:
        mid = (low + high)//2
        if li[mid] == target:
            return mid
        elif target > li[mid]:
            low = mid + 1
        else:
            high = mid - 1
    return -1
li = list(map(int,input().split()))
target = int(input())
print(Binary_Search(li,target))

