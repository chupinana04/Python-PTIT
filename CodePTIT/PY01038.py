if __name__ == '__main__':
    for t in range(int(input())):
        n = int(input())
        cnt = 0
        while n % 7 != 0:
            if cnt == 1000:
                break
            n += int(str(n)[::-1])
        print(n)