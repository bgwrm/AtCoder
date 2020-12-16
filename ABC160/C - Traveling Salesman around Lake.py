k, n = (int(_) for _ in input().split())
a = [int(_) for _ in input().split()]
d = [0] * n

for i in range(n-1):
    d[i] = a[i+1]-a[i]
d[n-1] = min(a[n-1]-a[0], k-a[n-1]+a[0])

print(k-max(d))