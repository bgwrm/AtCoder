import bisect
n, m = (int(_) for _ in input().split())
l = [[] for _ in range(n)]
ans = 0
for _ in range(m):
    a, b = (int(_) for _ in input().split())
    l[a-1] += [b-1]
    l[b-1] += [a-1]
for i in range(n):
    s = sorted(l[i])
    if bisect.bisect_left(s, i+1) == 1:
        ans += 1
print(ans)