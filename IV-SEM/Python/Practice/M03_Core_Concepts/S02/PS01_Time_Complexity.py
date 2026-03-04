"""
Set:
1. Use {} to create a set
2. Set does not allow duplicate values
3. Set is Unindexed
4. 1 is not allowed in the set if there are boolean values
5. Set is unordered
6. Set is heterogenious
7. Set is mutable

s = {1,True,20,12,13,12,14.5,9+8j}
print(s,type(s))
print(s[3])

# Adding elements in to the set
A = {1,2,3}
B = {3,4,5}
A.add(4)
B.update({6,7})
print(A,B)

# Removing Element
A.pop()
print(A)
A.remove(3)
A.difference(B)
B.difference(A)
print(A,B)
print(help("Set"))


Tuples:
1. Ordered and immutable collection of data
2. () represents tuple
3. Immutable
4. Accessing --> Index positions +ve or -ve
5. Nesteing of tuples --> tuple inside a tuple
6. Repitation
7. Slicing



t = (10,23,50,12,38,19)
t2 = ("anji","Ram","Ramanji")
print(t[0])
print(t[-1])
print(t + t2)
print(t,t2)
print(t*5)
print(t[:-1])
del t

#249
nums1 = [1,2,2,1]
nums2 = [2,2]

Set_nums1 = set(nums1)
Set_nums2 = set(nums2)
common = list(Set_nums1 & Set_nums2)
print(common)

# 657

class Solution:
    def judgeCircle(self, moves: str) -> bool:
            position = (0,0)
            x,y = position
            for move in moves:
                if move == 'U':
                    y += 1
                elif move == 'D':
                    y -= 1
                elif move == 'L':
                    x -= 1
                elif move == 'R':
                    x += 1
            position = (x,y)
            return position == (0,0)

            

# Dictionary
1. Creation
2. Accessing
3. Inserting
4. Deletion -->1) del -->
               2) pop()--> removes key returns value
               3) popitem() --> removes last inserted element
               4) clear() --> removes the entire dictionary
"""
d = {"a":"Anji"}
print(d)
d2 = dict(a='Anji',b='Ram',c='Ramanji')
print(d2)
print(d2.get('b'))
print(d2.keys())
print(d2.values())
print(d2={"age":25})
# 242 leet code
