n = int(input())
r = [int(_) for _ in input().split()]
ans = d = 0
for i in range(n-1):
    now = r[i+1]-r[i]
    if (now < 0 and d > 0) or (now > 0 and d < 0):
        ans += 1
    if now != 0:
        d = now
print(ans+2 if ans != 0 else ans)