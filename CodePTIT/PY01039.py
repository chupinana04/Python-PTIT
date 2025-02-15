def check(s):
    a = int(s[0])
    b = int(s[1])
    for i in range(2, len(s)):
        if int(s[i]) != a and int(s[i]) != b:
            return "NO"
        if s[i] == s[i-1]:
            return "NO"
    return "YES"

if __name__ == '__main__':
    for t in range(int(input())):
        s = input()
        print(check(s))