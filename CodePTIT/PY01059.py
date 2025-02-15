def solve(s):
    tong, tich = 0, 1
    check = False
    for i in range(len(s)):
        if i % 2 == 0:
            tong += int(s[i])
        else:
            if s[i] != '0':
                tich *= int(s[i])
                check = True
    if check == False:
        tich = 0
    return tong, tich
if __name__ == '__main__':
    for t in range(int(input())):
        s = input()
        tong, tich = solve(s)
        print(tong, tich)