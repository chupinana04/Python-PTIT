if __name__ == '__main__':
    n = int(input())
    matrix = []
    for i in range(n):
        row = list(map(int, input().split()))
        matrix.append(row)
    k = int(input())
    sum_top, sum_bot = 0, 0
    for i in range(n):
        for j in range(n):
            if i + j + 1 < n:
                sum_top += matrix[i][j]
            elif i + j + 1 > n:
                sum_bot += matrix[i][j]
    res = abs(sum_bot - sum_top)
    print("YES" if res <= k else "NO", res, sep = "\n")

