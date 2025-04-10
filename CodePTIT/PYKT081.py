def check(s):
    res = list(map(int, s.split('.')))
    if len(res) != 4:
        return "NO"
    for i in res:
        if i < 0 or i > 255:
            return "NO"
    return "YES"
if __name__ == "__main__":
    for t in range(int(input())):
        try:
            s = input()
            print(check())
        except: print("NO")