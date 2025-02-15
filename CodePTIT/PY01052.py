from math import *
def check_prime(n):
    if n < 2:
        return False
    for i in range(2, isqrt(n) + 1):
        if n % i == 0:
            return False
    return True
if __name__ == '__main__':
    for t in range(int(input())):
        n = sum(int(i) for i in input())
        print("YES" if check_prime(n) else "NO")