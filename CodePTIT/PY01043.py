def check(s):
    s1 = s[::-1]
    if s != s1 or len(s) % 2 != 0: return False
    for i in range(len(s)):
        if int(s[i]) % 2 != 0:
            return False
    return True
if __name__ == '__main__':
    for t in range(int(input())):
        n = int(input())
        for i in range(22, n, 2):
            if check(str(i)):
                print(i, end = " ")
        print()
