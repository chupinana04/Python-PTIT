from math import *
for t in range(int(input())):
    n, x, m = map(float, input().split())
    #cong thuc tinh lai kep  m = n * (1 + x%)^res
    res = log(m / n, 1 + x / 100)
    print(ceil(res))