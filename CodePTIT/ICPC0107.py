def solve(p, q, x1, x2):
    x1 = x1.replace(p, q)
    x2 = x2.replace(p, q)
    return int(x1) + int(x2)
if __name__ == "__main__":
    for t in range(int(input())):
        p, q = input().split()
        s = input().split()
        if len(s) > 1: x1, x2 = s[0], s[1]
        else:
            x1 = s[0]
            x2 = input()
        total_min = solve(p, q, x1, x2)
        total_max = solve(q, p, x1, x2)
        print(total_max, total_min)