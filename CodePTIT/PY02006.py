def check(arr1, arr2):
    for i in range(len(arr1)):
        if arr1[i] > arr2[i]:
            return "NO"
    return "YES"
if __name__ == '__main__':
    for t in range(int(input())):
        n = int(input())
        arr1 = list(map(int, input().split()))
        arr2 = list(map(int, input().split()))
        arr1.sort()
        arr2.sort()
        print(check(arr1, arr2))
