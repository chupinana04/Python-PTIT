from math import *
def check_prime(n):
    if n < 2:
        return False
    for i in range(2, isqrt(n) + 1):
        if n % i == 0:
            return False
    return True
def check(s):
    if check_prime(len(s)) == False:
        return False
    cnt_prime = 0
    for i in range(len(s)):
        if check_prime(int(s[i])) == True:
            cnt_prime += 1
    if cnt_prime < len(s) // 2:
        return False
    return True

if __name__ == '__main__':
    for t in range(int(input())):
        s = input()
        print("YES" if check(s) else "NO")