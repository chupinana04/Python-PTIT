from math import *
def nt(n):
    if n < 2: return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:  return False
    return True
def tong(n):
    sum = 0
    while n > 0:
        sum += n % 10
        n //= 10
    return sum
if __name__ == "__main__":
    for t in range(int(input())):
        a, b = map(int, input().split())
        x = gcd(a, b)
        '''if nt(tong(x)):
            print("YES")
        else:    print("NO")'''
        if nt(sum(int(i) for i in str(x))):
            print("YES")
        else:   print("NO")