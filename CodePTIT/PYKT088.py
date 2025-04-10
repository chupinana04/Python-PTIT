# de co 9 uoc so có 2 th :số đó có dạng p^8 hoặc (p^2 * q ^ 2) với p, q là snt
from math import isqrt


def sang_nt(n):
    primes = []
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, n + 1):
        if is_prime[i]:
            primes.append(i)
            for j in range(i * i, n + 1, i):
                is_prime[j] = False
    return primes
def solve(n):
    primes = sang_nt(isqrt(n))
    cnt = 0
    for i in primes:
        if i ** 8 <= n:
            cnt += 1
        else:
            break
    for i in range(len(primes)):
        for j in range(i + 1, len(primes)):
            if (primes[i] ** 2) * (primes[j] ** 2) <= n:
                cnt += 1
            else:
                break
    return cnt
if __name__ == "__main__":
    print(solve(int(input())))