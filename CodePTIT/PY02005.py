if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    cnt = 0
    for i in range(n):
        for j in range(i + 1, n):
            if arr[j] < arr[i]:
                cnt += 1
    print(cnt)