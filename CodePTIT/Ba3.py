import re
if __name__ == "__main__":
    n = int(input())
    freq = {}
    for i in range(n):
        s = input().lower()
        for word in re.split("[^a-z0-9]", s):
            if word != '':
                if word not in freq:
                    freq[word] = 1
                else:
                    freq[word] += 1
    ans = sorted(freq, key = lambda x : (-freq[x], x))
    for i in ans:
        if freq[i]:
            print(i, freq[i])