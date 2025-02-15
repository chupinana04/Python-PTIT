from math import *
if __name__ == '__main__':
    for t in range(int(input())):
        s1 = input()
        s2 = s1[::-1]
        if gcd(int(s1), int(s2)) == 1:
            print("YES")
        else:
            print("NO")