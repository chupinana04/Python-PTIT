from itertools import combinations

if __name__ == '__main__':
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    sort_arr = sorted(set(arr))
    for i in combinations(sort_arr, k):
        print(*i)