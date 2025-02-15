if __name__ == '__main__':
    for t in range(int(input())):
        b = int(input())
        s = input()
        decimal = int(s, 2)
        if b == 2:
            print(decimal)
        if b == 4:
            print(oct(decimal))
        if b == 8:
            print(oct(decimal))
        if b == 16:
            res = hex(decimal).upper()
            print(res)

