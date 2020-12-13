import math

n, m = (int(_) for _ in input().split())
a = sorted([int(_) for _ in input().split()])
k = n
l = []
ans = 0

if m == 0:
    print(1)
    exit()

a.insert(0, 0)
a.append(n+1)

for i in range(m+1):
    if a[i+1]-a[i] != 1:
        k = min(k, a[i+1]-a[i]-1)
        l.append(a[i+1]-a[i]-1)

for b in l:
    ans += math.ceil(b/k)

print(ans)