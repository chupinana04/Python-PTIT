from collections import Counter
if __name__ == "__main__":
    n = int(input())
    list_string = []
    for i in range(n):
        list_string.append(input())
    freq = Counter(list_string)
    print(len(freq))

