h, w = (int(_) for _ in input().split())
a = [[int(_) for _ in input().split()] for i in range(h)]
b = [[int(_) for _ in input().split()] for i in range(h)]
c = [[] for _ in range(h)]
ans = 0
for i in range(h):
    for j in range(w):
        c[i] += [a[i][j]-b[i][j]]
for i in range(h-1):
    for j in range(w-1):
        p = c[i][j]
        ans += abs(p)
        c[i][j] -= p
        c[i+1][j] -= p
        c[i][j+1] -= p
        c[i+1][j+1] -= p
    if sum(c[i]) != 0:
        exit(print('No'))
print('Yes')
print(ans)