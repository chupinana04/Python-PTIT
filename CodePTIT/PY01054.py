if __name__ == '__main__':
    for t in range (int(input())):
        s = input()
        tich = 1
        for i in s:
            if i == '0':
                continue
            tich *= int(i)
        print(tich)