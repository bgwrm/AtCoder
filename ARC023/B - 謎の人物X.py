r, c, d = (int(_) for _ in input().split())
a = [[int(_) for _ in input().split()] for i in range(r)]
ans, p = 0, d%2
for i in range(r):
    for j in range(c):
        if i+j <= d and (i+j)%2 == p:
            ans = max(a[i][j], ans)
print(ans)