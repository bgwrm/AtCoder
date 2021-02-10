from collections import Counter
n = int(input())
d = [int(_) for _ in input().split()]
ans, c = 1, Counter(d)
if d[0] != 0 or d.count(0) != 1:
    exit(print(0))
for i in range(1, max(d)+1):
    ans *= c[i-1] ** c[i]
    ans %= 998244353
print(ans)