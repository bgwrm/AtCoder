n, m, x = (int(_) for _ in input().split())
ca = [[int(_) for _ in input().split()] for i in range(n)]
ans = 10**9

for i in range(1, 2**n):
    l = [0]*(m+1)
    for j in range(n):
        if(i>>j)&1:
            for k in range(m+1):
                l[k] += ca[j][k]
    if min(l[1:]) >= x:
        ans = min(ans, l[0])

print(-1 if ans == 10**9 else ans)