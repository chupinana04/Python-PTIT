import math
if __name__ == "__main__":
    n = int(input())
    a = []
    for t in range(n):
        res = [str(i) for i in input()]
        a.append(res)
    cnt = 0
    r, c = [0] * n, [0] * n
    for i in range(n):
        cnt_x = 0
        for j in range(n):
           if a[i][j] == 'C':
                r[i] += 1
                c[j] += 1
    for i in range(n):
        cnt += math.comb(r[i], 2)
        cnt += math.comb(c[i], 2)
    print(cnt)


