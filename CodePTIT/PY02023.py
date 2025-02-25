def sum_of_digits(n):
    return sum(int(n) for n in str(n))
def sort(arr):
    return sorted(arr, key= lambda x:(sum_of_digits(x), x))
if __name__ == '__main__':
    for t in range(int(input())):
        n = int(input())
        arr = list(map(int, input().split()))
        result = sort(arr)
        print(*result)

