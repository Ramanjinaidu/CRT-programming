from typing import List


def collatz_sequence(n: int) -> list:
    sequence = []
    
    while n != 1:
        sequence.append(n)
        
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
    
    sequence.append(1)
    return sequence


if __name__ == '__main__':
    n = int(input())
    print(collatz_sequence(n))