"""
Data Types:
1.Fundamental DT:
    1.int
    2.float
    3.complex
    4.Boolean
    5.String
2.Collection DT:
    1.List
    2.Tuple
    3.Set
    4.Dictionary
* In python complex numbers are represented in the form of a+bj (here j is complex)
"""
x = 10
y = 12.5
z = 4 + 5j
print(x,type(x))
print(y,type(y))
print(z,type(z))

f1 = 3e2
f2 = 4E3
print(f1,type(f1))
print(f2,type(f2))

c1 = 4 + 6j
c2 = complex(2,-4)
print(c1 + c2)
print(c1 - c2)
print(c1 * c2)
print(c1 / c2)

print(c1.real)
print(c2.imag)

# Indexing using Slicing
s = "Python"
print(s[2])         # prints charecter at 2 index string
print(s[::])        # prints entire string
print(s[::2])       # prints the string by increase step by 2
print(s[::-1])      # prints the string in reverse order