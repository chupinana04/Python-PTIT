if __name__ == '__main__':
    n = int(input())
    matrix = []
    for i in range(n):
        hang = list(map(int, input().split()))
        matrix.append(hang)
    k = int(input())
    sum_top = 0
    sum_bot = 0
    for i in range(n):
        for j in range(n):
            if i > j:
                sum_top += matrix[i][j]
            elif i < j:
                sum_bot += matrix[i][j]
    res = abs(sum_top - sum_bot)
    if(res <= k):
        print("YES", res, sep = "\n")
    else:
        print("NO", res, sep = "\n")
