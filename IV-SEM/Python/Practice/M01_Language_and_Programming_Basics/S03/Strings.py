"""
li = [1,2,3,4,5]
res = []
for i in li:
    if i%2 == 0:
        res.append(i)
print(res)
# Comprahentions

li = [1,2,3,4,5]
print([i for i in li if i%2 == 0])
print(tuple(i for i in li if i%2 == 0))
print({i:i*2 for i in li if i%2 == 0})
"""

# Joining Strings


# li1 = ['a','b','c']
# res = " "
# for ch in li1:
#     res += ch + " "
# print(res)
li1 = ['a','b','c']
print(" ".join(li1))