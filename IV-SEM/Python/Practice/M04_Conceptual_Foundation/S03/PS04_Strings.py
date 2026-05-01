# Biult-in functions
"""
s = "Python"
print(len(s))
print(max(s))
print(min(s))
print(max("abc123ABC"))

# Buit-in methods
s = "python"
s = s.replace("y","Y")
print(s)
print(s.find("on"))
print(s.find("xyz"))
#reverse a string without using slicing

s = "python"
rev = ""
for i in range(len(s)-1,-1,-1):
    rev += s[i]
print(rev)
if s==rev:
    print("p")
else:
    print("no")
"""

#Anagram
s1="paces"
s2="space"
if sorted(s1) == sorted(s2):
    print("Anagram")
else:
    print("Not an anagram")

from collections import Counter
s1 = input()
s2 = input()
if Counter(s1) == counter(s2):
    print("Anagram")
else:
    print("Not Anagram")

