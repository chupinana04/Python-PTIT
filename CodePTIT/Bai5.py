if __name__ == "__main__":
    for t in range(int(input())):
        n = int(input())
        arr = list(map(int, input().split()))
        arr.sort()
        cnt = 0
        for i in range(n - 2):
            l = i + 1
            r = n - 1
            while l < r:
                res = arr[i] + arr[l] + arr[r]
                if res == 0:
                    cnt += 1
                    l += 1
                elif res < 0:
                    l += 1
                else:
                    r -= 1
        print(cnt)
