def check(s):
    for i in range(len(s)):
        if i == 2 or i == 3 or i == 5 or i == 7:
            if s[i] != '2' and s[i] != '3' and s[i] != '5' and s[i] != '7':
                return "NO"
        if i == 0 or i == 1 or i == 4 or i == 6 or i == 8 or i == 9:
            if s[i] == '2' or s[i] == '3' or s[i] == '5' or s[i] == '7':
                return "NO"
    return "YES"
if __name__ == '__main__':
    for t in range(int(input())):
        s = input()
        print(check(s))
