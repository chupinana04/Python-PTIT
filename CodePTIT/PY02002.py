def fibo():
    f = [1] * 93
    for i in range(3, 93):
        f[i] = f[i - 1] + f[i - 2]
    return f
if __name__ == '__main__':
    fib_list = fibo()
    for t in range(int(input())):
        a, b = map(int, input().split())
        for num in range(a, b + 1):
            print(fib_list[num], end=' ')
        print()
