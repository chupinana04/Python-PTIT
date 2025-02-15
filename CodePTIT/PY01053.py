if __name__ == '__main__':
    for t in range(int(input())):
        s = input()
        n = sum(int(i) for i in s)
        if n % 3 == 0:
            print("YES")
        else:
            print("NO")