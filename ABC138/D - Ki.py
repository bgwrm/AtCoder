n, q = (int(_) for _ in input().split())
ans, check, g, l = [0]*n, [1]+[0]*(n-1), [[] for _ in range(n)], [0]
for _ in range(n-1):
    a, b = (int(_) for _ in input().split())
    g[a-1] += [b-1]
    g[b-1] += [a-1]
for _ in range(q):
    p, x = (int(_) for _ in input().split())
    ans[p-1] += x
while l:
    t = l.pop()
    for u in g[t]:
        if check[u] == 0:
            ans[u] += ans[t]
            l += [u]
            check[u] = 1
print(*ans)