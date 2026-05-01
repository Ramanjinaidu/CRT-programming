# # Digital Root
# def Digital_Root(n):
#     if n < 10:
#         return n
#     for i in str(n):
#         s = sum(int(i))
#         return Digital_Root(s)
# print(Digital_Root(245))

# check if array is sorted or not
def Sorted_Array(nums):
    if nums.sort() == nums:
        return True
    else:
        return False
print(Sorted_Array([10,20,30,40,50]))