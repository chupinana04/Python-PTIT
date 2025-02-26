import math
def check(n):
    s = str(n)
    res = 0
    for i in s:
        res += math.factorial(int(i))
    if res == n:
        return "Yes"
    return "No"
if __name__ == "__main__":
    for t in range(int(input())):
        n = int(input())
        print(check(n))