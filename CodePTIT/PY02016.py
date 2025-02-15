if __name__ == '__main__':
    for t in range(int(input())):
        n = int(input())
        a = list(map(int, input().split()))
        frequency = {}
        for x in a:
            if x not in frequency:
                frequency[x] = 1
            else:
                frequency[x] += 1
        max_value = max(frequency.values())
        min_value = min(x for x in a if frequency[x] == max_value)
        if max_value <= (n/2):
            print("NO")
        else:
            print(min_value)
