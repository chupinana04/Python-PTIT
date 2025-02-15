def check(s):
    if len(s) < 3:
        return "NO"
    i = 0
    while i < len(s) - 1 and s[i] < s[i+1]:
        i += 1
    if i == 0 or i == len(s) - 1:
        return "NO"
    while i < len(s) - 1 and s[i] > s[i+1]:
        i += 1
    if i != len(s) - 1:
        return "NO"
    return "YES"
if __name__ == '__main__':
    for t in range (int(input())):
        s = input()
        print(check(s))