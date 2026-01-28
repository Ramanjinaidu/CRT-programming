#1. Count the number of digits in a given number.
# n = int(input())
# temp = n
# count = 0
# while n>0:
#     count += 1
#     n = n // 10
# print(count)
# print(len(str(temp)))

#2. Finding sum of digits in a number

# n = int(input())
# s = 0
# while n>0:
#     s += n%10
#     n = n//10
# print(s)

#3. Count even digits and odd digits of a number

# n = int(input())
# even_count = 0
# odd_count = 0
# ev_sum = 0
# od_sum = 0
# while n>0:
#     digit = n%10
#     if digit%2 == 0:
#         even_count += 1
#         ev_sum += digit

#     else:
#         odd_count += 1
#         od_sum += digit
#     n = n//10
# print("Even digits:", even_count)
# print("Odd digits:", odd_count)
# print("Even_Sum:",ev_sum)
# print("Odd_Sum:",od_sum)

#4. add digits of a number until the sum becomes single digit.

n = int(input())
while n > 10:
    n = sum(list(map(int,str(n))))
print(n)

            