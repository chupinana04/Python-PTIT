from math import *
def isPrime(n):
    if n < 2:   return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False

    return True
for t in range(int(input())):
    n = int(input())
    cnt = 0
    for i in range(1, n):
        if gcd(i, n) == 1:
            cnt += 1
    if isPrime(cnt):
        print("YES")
    else:   print("NO")