def solve(n):
    values = set()
    while n != 1:
        values.add(n)
        if n % 2 == 0:
            n //= 2
        else:
            n = n * 3 + 1
    values.add(1)
    return len(values)
while True:
    n = int(input())
    if n == 0:
        break
    print(solve(n))
