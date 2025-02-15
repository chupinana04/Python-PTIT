if __name__ == '__main__':
    for t in range(int(input())):
      s = input()
      a = int(s[len(s) - 2: len(s)])
      if a == 86:
        print("YES")
      else:
        print("NO")