if __name__ == "__main__":
    for t in range(int(input())):
        n, m = map(int, input().split())
        matrix = [[0]] * n
        kenel = [[0]] * 3
        for i in range(n): matrix[i] = [int(x) for x in input().split()]
        for i in range(3): kenel[i] = [int(x) for x in input().split()]
        res = 0
        for i in range(2, n):
            for j in range(2, m):
                res += matrix[i - 2][j - 2] * kenel[0][0]
                res += matrix[i - 2][j - 1] * kenel[0][1]
                res += matrix[i - 2][j] * kenel[0][2]
                res += matrix[i - 1][j - 2] * kenel[1][0]
                res += matrix[i - 1][j - 1] * kenel[1][1]
                res += matrix[i - 1][j] * kenel[1][2]
                res += matrix[i][j - 2] * kenel[2][0]
                res += matrix[i][j - 1] * kenel[2][1]
                res += matrix[i][j] * kenel[2][2]
        print(res)