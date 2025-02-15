if __name__ == '__main__':
    for t in range(int(input())):
        n = int(input())
        a = [int(input()) for _ in range(n)]
        frequency = {}
        for x in a:
            if x in frequency:
                frequency[x] += 1
            else:
                frequency[x] = 1
        max_count = max(frequency.values())
        min_value = min(x for x in frequency if frequency[x] == max_count)
        print(min_value)
