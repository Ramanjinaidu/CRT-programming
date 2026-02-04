n = int(input())
if n<5:
    print("Free")
elif 5<=n<=17:
    print("$",10)
elif 18<=n<=64:
   print("$",20)
elif n>=65:
   print("$",15)
else:
   print("Invalid Input")
