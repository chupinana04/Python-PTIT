from math import isqrt

p = [1] * 100001
def sangnt():
    p[0] = p[1] = 0
    i = 2
    for i in range(2, 1000):
        if p[i]:
            for j in range(i * i, 100001, i):
                p[j] = 0
if __name__ == "__main__":
    sangnt()
    for t in range(int(input())):
        n = int(input())
        ans = 0
        for i in range(3, n, 2):
            if p[i] and p[i - 6]and p[i - 2]:
                ans += 1
            if p[i] and p[i - 6]and p[i - 4]:
                ans += 1
        print(ans)