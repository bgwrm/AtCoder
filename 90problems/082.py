l, r = (int(_) for _ in input().split())
ans, now, rr, mod = 0, 1, r*(r+1), 10**9+7
for i in range(19):
    if r >= now:
        p = max(l, now)
        ans = (ans+(rr-p*(p-1))//2)%mod
        now *= 10
    else:
        break
print(ans)