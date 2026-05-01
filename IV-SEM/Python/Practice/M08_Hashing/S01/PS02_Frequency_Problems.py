# Frequency of each element in the array
#[1,2,3,4,5,2,3,1,1] ==> {1:3,2:3,3:1,4:1,5:1}

arr = list(map(int,input().split()))
freq = {}
for i in arr:
    freq[i] = freq.get(i,0) + 1
print(freq)
# Find the element with maximum frequency
from collections import Counter
li = list(map(int,input().split()))
freq = dict(Counter(li))
print(max(freq,key = freq.get))