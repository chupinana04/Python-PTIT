def check(s):
    sum = int(s[0])
    for i in range(1, len(s)):
        if abs(ord(s[i]) - ord(s[i-1])) != 2:
            return "NO"
        sum += int(s[i])
    if sum % 10 != 0:
        return "NO"
    return "YES"
if __name__ == '__main__':
    for t in range(int(input())):
        s = input()
        print(check(s))