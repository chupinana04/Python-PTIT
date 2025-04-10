def solve(s):
    cnt = 0
    for i in s:
        if i == '4' or i == '7':   cnt += 1
    if cnt == 4 or cnt == 7:    return "YES"
    return "NO"
if __name__ == "__main__":
    s = input()
    print(solve(s))