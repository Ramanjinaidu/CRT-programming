A = int(input("Enter a Number:"))
if A < 0:
    print("Number Invalid")
else:
    if A%2 !=0:
        print("Weird")
    elif A%2 == 0 and 6<=A<=20:
        print("Weird")
    elif A%2 == 0 and 2<=A<=5 and A>20:
        print("Not Weird")