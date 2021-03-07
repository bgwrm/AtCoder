n, m = (int(_) for _ in input().split())
a = [int(_) for _ in input().split()]
l = [0]*(n+1)
for i in a[:m]:
    l[i] += 1
ans = l.index(0)
for i in range(n-m):
    l[a[i]] -= 1
    l[a[i+m]] += 1
    if l[a[i]] == 0:
        ans = min(a[i], ans)
print(ans)