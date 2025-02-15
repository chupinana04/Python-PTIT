def check(s):
    for i in range(len(s) - 1):
        if s[i] > s[i+1]: return False
    return True
if __name__ == '__main__':
    for t in range(int(input())):
        s = input()
        if check(s):
            print("YES")
        else:
            print("NO")