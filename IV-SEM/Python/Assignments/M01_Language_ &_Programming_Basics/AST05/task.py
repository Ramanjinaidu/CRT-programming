from typing import List

def Collatz_Sequence(n: int) -> List:
    res = []
    while True:
        res.append(n)
        if n == 1:
            break
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
    return res

if __name__ == '__main__':
    n = int(input())
    print(Collatz_Sequence(n))