def to_base(n, base):
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if n == 0:
        return "0"
    result = ""
    while n > 0:
        result = digits[n % base] + result
        n //= base
    return result

if __name__ == "__main__":
    f = open("DATA.in", 'r')
    for t in range(int(f.readline())):
        b = int(f.readline())
        s = f.readline().strip()
        n = int(s, 2)
        #print(n) chuyen chuoi s tu dang nhi phan sang tp
        print(to_base(n, b))