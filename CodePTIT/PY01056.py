from math import isqrt


def check_prime(n):
    if n < 2:
        return False
    for i in range(2, isqrt(n) + 1):
        if n % i ==0:
            return False
    return True
def check(s):
    tong = sum(int(i) for i in s)
    if check_prime(tong) == False:
        return "NO"
    for i in range(len(s)):
        if i % 2 == 0 and int(s[i]) % 2 != 0:
            return "NO"
        if i % 2 != 0 and int(s[i]) % 2 == 0:
            return "NO"
    return "YES"
if __name__ == '__main__':
    for t in range(int(input())):
        s = input()
        print(check(s))