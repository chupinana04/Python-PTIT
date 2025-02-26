from math import isqrt
def solve(n):
    s1 = str(n)
    s2 = s1[::-1]
    total = sum(int(i) for i in s1)
    if not check_prime(n) or not check_prime(int(s2)) or not check_prime(total):
        return "No"
    for i in s1:
        if not check_prime(int(i)):
            return "No"
    return "Yes"

def check_prime(n):
    if n < 2: return False
    for i in range(2, isqrt(n) + 1):
        if n % i == 0:
            return False
    return True

if __name__ == "__main__":
    for t in range(int(input())):
        n = int(input())
        print(solve(n))
