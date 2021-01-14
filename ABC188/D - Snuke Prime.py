n, c = (int(_) for _ in input().split())
l = []
pre = now = ans = 0
for i in range(n):
    a, b, f = (int(_) for _ in input().split())
    l += [[a, f], [b+1, -f]]
l = sorted(l)
for day, fee in l:
    ans += min(c, now)*(day-pre)
    now += fee
    pre = day
print(ans)