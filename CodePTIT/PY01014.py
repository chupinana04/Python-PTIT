a, k, n = map(int, input().split())
b = k - a % k
check = False
for i in range(a + b, n + 1, k):
     print(i - a, end = ' ')
     check = True
if not check:
    print(-1)