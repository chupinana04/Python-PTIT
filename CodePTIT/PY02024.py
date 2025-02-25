def tich(n):
    res = 1
    s = str(n)
    for i in s:
        res *= int(i)
    return res
def sort_tich(arr):
    return sorted(arr, key = lambda x:(tich(x), x))
if __name__ == '__main__':
    for t in range(int(input())):
        n = int(input())
        arr = list(map(int, input().split()))
        result = sort_tich(arr)
        print(*result)
