n, k = (int(_) for _ in input().split())
a = [int(_) for _ in input().split()]
now, t, s =1, [1], {1}
for i in range(n):
    now = a[t[i]-1]
    if now in s:
        break
    t += [now]
    s.add(now)
if k >= len(t):
    b = t.index(now)
    k = (k-b)%(len(t)-b)+b
print(t[k])