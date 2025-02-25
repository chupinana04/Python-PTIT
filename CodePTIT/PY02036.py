from math import *
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    for i in range(n):
        for j in range(i + 1, n):
            if gcd(arr[i], arr[j]) == 1:
                print(arr[i], arr[j], end = " ")
                print()