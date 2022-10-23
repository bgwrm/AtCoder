n, q = (int(_) for _ in input().split())
senbei = [0]*(n+1)
ans, now = 0, 0
for _ in range(q):
    l, r = (int(_) for _ in input().split())
    senbei[l-1] += 1
    senbei[r] -= 1
for i in range(n):
    now = (now+senbei[i])%2
    ans += now
print(ans)