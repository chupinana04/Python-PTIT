from math import *
if __name__ == '__main__':
    for t in range(int(input())):
        n = int(input())
        res = "1 * "
        for i in range(2, isqrt(n) + 1):
            if n % i == 0:
                cnt = 0
                while n % i == 0:
                    n //= i
                    cnt += 1
                res += str(i) + "^" + str(cnt) + " * "
        if n != 1:
            res += str(n) + "^1"
        else:
            res = res[:-2]
        print(res)