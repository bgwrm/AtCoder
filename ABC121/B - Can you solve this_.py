n, m, c = (int(_) for _ in input().split())
b = [int(_) for _ in input().split()]
a = [[int(_) for _ in input().split()] for i in range(n)]
ans = 0

for i in range(n):
    p = c
    for j in range(m):
        p += a[i][j] * b[j]
    if p > 0:
        ans += 1

print(ans)