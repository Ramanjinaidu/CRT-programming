def Array_Sum(nums):
    s = 0
    for i in range(len(nums)):
        s += nums[i]
    return s
print(Array_Sum([10,20,30,40]))

def Array_Sum1(nums):
    if len(nums) == 0:
        return 0
    else:
        return nums[-1] + Array_Sum1(nums[:-1])
print(Array_Sum1([10,20,30,40]))

# Reverse the list using recursion

def Array_Rev(nums):
    rev = []
    for i in range(len(nums)-1,-1,-1):
        rev.append(nums[i])
    return rev
print(Array_Rev([10,20,30,40,50]))

def Reverse_Array(nums,i,j):
    if i >= j:
        return
    nums[i],nums[j] = nums[j],nums[i]
    Reverse_Array(nums,i+1,j-1)
    return nums
print(Reverse_Array([1,2,3,4,5],0,4))

def Reverse_String(S):
    rev = ""
    for i in range(len(S)-1,-1,-1):
        rev += S[i]
    return rev
def is_palindrome(S):
    return S == Reverse_String(S)
print(Reverse_String("python"))
print(is_palindrome("abc"))
print(is_palindrome("madam"))