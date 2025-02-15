s = input()
res1 = 0
res2 = 0
for i in range(len(s)):
    if s[i].islower(): res1 += 1
    else: res2 += 1
if res1 >= res2: print(s.lower())
else: print(s.upper())