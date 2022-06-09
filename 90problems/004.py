h, w = (int(_) for _ in input().split())
a = [[int(_) for _ in input().split()] for i in range(h)]
row, col = [0]*h, [0]*w
for i in range(w):
    col[i] = sum([a[j][i] for j in range(h)])
for i in range(h):
    row[i] = sum(a[i])
for i in range(h):
    print(*[row[i]+col[j]-a[i][j] for j in range(w)], sep=' ')