n = int(input())
a = [int(_) for _ in input().split()]
p, pmax, now, ans = 0, 0, 0, 0
for i in a:
    p += i
    pmax = max(pmax, p)
    ans = max(ans, now+pmax)
    now += p
print(ans)