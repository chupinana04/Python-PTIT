from collections import Counter
if __name__ == "__main__":
    arr = []
    for t in range(int(input())):
        arr.append(input())
    arr = Counter(arr)
    print(len(arr))