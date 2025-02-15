P = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_."
while True:
    str = input()
    if str == "0":
        break
    k, s = str.split()
    k = int(k)
    res = ""
    for i in range(len(s)):
        index = P.find(s[i])
        res += P[(index + k) % 28]
    print(res[::-1])