from xmlrpc.client import MININT

if __name__ == '__main__':
    for t in range(int(input())):
        s = input()
        ans = MININT
        i = 0
        while i < len(s):
            if s[i].isdigit():
                found_digit = True
                res = 0
                while i < len(s) and s[i].isdigit():
                    res = res * 10 + int(s[i])
                    i += 1
                ans = max(ans, res)
            else:
                i += 1
        print(ans)