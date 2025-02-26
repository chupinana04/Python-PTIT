if __name__ == "__main__":
    for t in range(int(input())):
        n, d = map(int, input().split())
        arr = list(map(int, input().split()))
        print(*arr[d::], *arr[:d:])