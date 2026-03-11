def sum_of_digits(n: int) -> int:
    sum_n = 0
    while n>0:
        digit = n%10
        sum_n += digit
        n = n//10
    return sum_n

if __name__ == "__main__":
    n = int(input())
    print(sum_of_digits(n))
