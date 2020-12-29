import math
t = [int(input()) for _ in range(5)]
fp = []
ans = 0

for i in t:
    ans += math.ceil(i/10) * 10
    if i%10 != 0:
        fp += [i%10]

if len(fp) > 0:
    ans += min(fp) - 10

print(ans)