n, q = (int(_) for _ in input().split())
a = [int(_) for _ in input().split()]
now, d = 0, [0]*(n-1)
for i in range(n-1):
    d[i] = a[i+1]-a[i]
    now += abs(d[i])
for _ in range(q):
    l, r, v = (int(_) for _ in input().split())
    if l != 1:
        now += abs(d[l-2]+v)-abs(d[l-2])
        d[l-2] += v
    if r < n:
        now += abs(d[r-1]-v)-abs(d[r-1])
        d[r-1] -= v
    print(now)