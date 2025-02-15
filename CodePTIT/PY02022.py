from collections import Counter
from math import isqrt


def check_prime(num):
    if num < 2:
        return False
    for i in range(2, isqrt(num) + 1):
        if num % i == 0:
            return False
    return True
if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    f = Counter(a)
    a = list(dict.fromkeys(a))
    for i in a:
        if check_prime(i):
            print(i, f[i])
