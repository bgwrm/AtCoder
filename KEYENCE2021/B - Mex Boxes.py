from collections import Counter
n, k = (int(_) for _ in input().split())
a = Counter([int(_) for _ in input().split()])
ans, b, l = 0, n, len(set(a))
for i in range(l):
    b = min(a[i], b)
    ans += min(b, k)
print(ans)