def check(s):
    s = str(s)
    if len(s) % 2 == 1: return False
    for i in range(len(s)):
        if s[i] != '0' and s[i] != '2' and s[i] != '4' and s[i] != '6' and s[i] != '8':
            return False
    res = s[::-1];
    if res != s: return False
    return True
if __name__ == '__main__':
    for t in range(int(input())):
        n = int(input())
        for i in range(22, n, 2 ):
            if check(i):
                print(i, end = " ")
        print()