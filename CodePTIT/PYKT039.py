def check(a, b):
    for i in range(len(a)):
        if a[i] > b[i]: return False
    return True
if __name__ == "__main__":
    for t in range(int(input())):
        n = int(input())
        a = list(map(int, input().split()))
        b = list(map(int, input().split()))
        a.sort()
        b.sort()
        print("YES" if check(a, b) else "NO")