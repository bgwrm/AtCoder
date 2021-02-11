h, w = (int(_) for _ in input().split())
c = [[int(_) for _ in input().split()] for i in range(10)]
ans = 0
for i in range(10):
    for j in range(10):
        for k in range(10):
            c[j][k] = min(c[j][i]+c[i][k], c[j][k])
for _ in range(h):
    for n in [int(_) for _ in input().split()]:
        if n > -1:
            ans += c[n][1]
print(ans)