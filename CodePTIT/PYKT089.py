if __name__ == "__main__":
    n = int(input())
    a = []
    while len(a) < n:
        a += [int(i) for i in input().split()]
    chan = []
    le = []
    b = [0] * n
    for i in range(len(a)):
        if a[i] % 2 == 0:
            chan.append(a[i])
        else:
            le.append(a[i])
            b[i] = 1
    chan = sorted(chan)
    le = sorted(le, reverse=True)
    for i in b:
        if i == 0:
            print(chan[0], end = " ")
            chan.pop(0)
        else:
            print(le[0], end = " ")
            le.pop(0)