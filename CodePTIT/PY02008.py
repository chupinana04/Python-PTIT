def sangNT():
    primes = [True] * (10000)
    primes[0] = False
    primes[1] = False
    p = 2
    while p * p <= 10000:
        if primes[p] == True:
            for i in range(p * p, 10000, p):
                primes[i] = False
        p += 1
    return primes
if __name__ == '__main__':
    primes = sangNT()
    a = [p for p in range(2, 10000) if primes[p]]
    n, x = map(int, input().split())
    for i in range(n + 1):
        print(x, end=' ')
        x += a[i]