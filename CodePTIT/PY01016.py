if __name__ == '__main__':
    for t in range(int(input())):
        s = input()
        '''for i in range(0, len(s), 2):
            for j in range(0, int(s[i + 1])):
                print(s[i], end='')
        print()'''
        res = ""
        for i in range(0, len(s), 2):
            res += s[i] * int(s[i + 1])
        print(res)
