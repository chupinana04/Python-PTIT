from math import *
if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    for i in range(n):
        for j in range(i + 1, n):
            if gcd(a[i], a[j]) == 1:
                print(a[i], a[j])