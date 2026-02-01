age = int(input("Age: "))
match age:
    case age if age < 5:
        print("Free")
    case age if age >= 5 and age <=17:
        print("$",10)
    case age if 18<= age <=64:
        print("$",20)
    case age if age >= 65:
        print("$",15)