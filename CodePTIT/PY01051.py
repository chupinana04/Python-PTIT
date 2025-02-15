def check(s):
    s1 = s[::-1]
    if s != s1: return False
    return True
if __name__ == '__main__':
    for t in range(int(input())):
        s = input()
        n = sum(int(i) for i in s)
        if n < 10:
            print("NO")
        else:
            if check(str(n)):
                print("YES")
            else:
                print("NO")