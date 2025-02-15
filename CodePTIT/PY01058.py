from math import isqrt


def check_prime(n):
    if n < 2:   return "NO"
    for i in range(2, isqrt(n) + 1):
        if n % i == 0:
            return "NO"
    return "YES"
if __name__ == '__main__':
    for t in range(int(input())):
        s = input()
        n = int(s[len(s) - 4::])
        print(check_prime(n))