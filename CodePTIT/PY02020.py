if __name__ == '__main__':
    n = int(input())
    a = list(map(float, input().split()))
    a.sort()
    min_value = min(a)
    max_value = max(a)
    cnt = 0.0
    res = 0.0
    for i in range(n):
        if a[i] != min_value and a[i] != max_value:
            cnt += 1
            res += a[i]
    print("%.2f" %(res/cnt))

