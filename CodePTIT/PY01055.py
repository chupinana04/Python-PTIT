def check(s):
    if len(s) % 2 == 0:
        return "NO"
    if s[0] == s[1]:
        return "NO"
    for i in range(0, len(s) - 1, 2):
        if s[i] != s[0]:
            return "NO"
    return "YES"
if __name__ == '__main__':
    for t in range(int(input())):
        s = input()
        print(check(s))