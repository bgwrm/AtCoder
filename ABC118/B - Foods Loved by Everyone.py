from collections import Counter
n, m = (int(_) for _ in input().split())
ka = [[int(_) for _ in input().split()] for i in range(n)]
l = []
ans = 0

for i in range(n):
    l += ka[i][1:]

for i in Counter(l).values():
    if i == n:
        ans += 1
print(ans)