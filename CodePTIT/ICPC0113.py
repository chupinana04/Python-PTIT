from math import isqrt


def check_prime(n):
    if n < 2: return False
    for i in range(2, isqrt(n) + 1):
        if n % i == 0:
            return False
    return True
def solve(i, n):
    s1 = str(i)
    s2 = s1[::-1]
    if int(s1) < int(s2) < n and check_prime(int(s1)) and check_prime(int(s2)):
        return True
    return False

if __name__ == "__main__":
    for t in range(int(input())):
        n = int(input())
        for i in range(13, n + 1):
            if(solve(i, n)):
                print(i, str(i)[::-1], end = " ")
        print()