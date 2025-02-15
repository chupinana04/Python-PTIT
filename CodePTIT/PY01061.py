from math import *
def check_prime(n):
    if n < 2:
        return False
    for i in range(2, isqrt(n) + 1):
        if n % i == 0:
            return False
    return True
if __name__ == '__main__':
    for t in range(int(input())):
        s = input()
        a = int(s[0:3:])
        b = int(s[len(s) - 3::])
        if(check_prime(a) and check_prime(b)):
            print("YES")
        else:
            print("NO")