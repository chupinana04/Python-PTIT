if __name__ == '__main__':
    arr = []
    while len(arr) < 10:
        arr += list(map(int, input().split()))
    for i in range(len(arr)):
        arr[i] %= 42
    arr = set(arr)
    print(len(arr))