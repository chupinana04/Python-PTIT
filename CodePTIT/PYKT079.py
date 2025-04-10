from Test import name
if __name__ == "__main__":
    for t in range(int(input())):
        n = int(input())
        arr = list(map(int, input().split()))
        res = dict(arr)
        print(res)
        print(Test.name())