class Matrix:
    def __init__(self, n, m, a):
        self.n = n
        self.m = m
        self.a = a
    def chuyenVi(self):
        res = [[0] * self.n for _ in range(self.m)]
        for i in range(self.m):
            for j in range(self.n):
                res[i][j] = self.a[j][i]
        return Matrix(self.m, self.n, res)
    def nhanChuyenVi(self):
        cvi = self.chuyenVi()
        res = [[0] * self.n for _ in range(self.n)]
        for i in range(self.n):
            for j in range(self.n):
                res[i][j] += sum(self.a[i][k] * cvi.a[k][j] for k in range(self.m))
        return res

if __name__ == "__main__":
    for t in range(int(input())):
        res = []
        while len(res) < 2:
            res += [int(x) for x in input().split()]
        n, m = res[0], res[1]
        res.clear()
        while len(res) < n * m:
            res += [int(x) for x in input().split()]
        a = [[0] * m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                a[i][j] = res[0]
                res.pop(0)
        matrix = Matrix(n, m, a)
        res = matrix.nhanChuyenVi()
        for i in range(n):
            print(*res[i])
        res.clear()

