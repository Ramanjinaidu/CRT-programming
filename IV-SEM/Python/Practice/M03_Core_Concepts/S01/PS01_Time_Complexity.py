def Linear_Search(elements,target):
    for i in range(len(elements)):
        if target == elements[i]:
            return i
    return -1

print(Linear_Search([12,13,14,15,16],12))
print(Linear_Search([12,13,14,15,16],60))
print(Linear_Search([12,13,14,15,16],14))

