def chuyen(s):
    res = 0
    for i in s: res += ord(i) - ord('0')
    return str(res)
if __name__ == "__main__":
    s = input()
    cnt = 0
    while(len(s) > 1):
        s = chuyen(s)
        cnt += 1
    print(cnt)

