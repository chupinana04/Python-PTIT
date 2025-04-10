if __name__ == "__main__":
    for t in range(int(input())):
        s = input()
        if len(s) >= 100:
            i = 100
            while s[i] != ' ':
                i -= 1
            s = s[:i]
        print(s)
