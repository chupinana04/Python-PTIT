arr = list(int(i) for i in input())
cnt = 0
for i in arr:
    if i == 4 or i == 7:
        cnt += 1
if cnt == 4 or cnt == 7:
    print("YES")
else:
    print("NO")