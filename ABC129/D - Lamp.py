h, w = (int(_) for _ in input().split())
s = [list(input()) for _ in range(h)]
yoko = [[0]*w for _ in range(h)]
tate = [[0]*w for _ in range(h)]
ans = 0
for i in range(h):
    c = 0
    for j in range(w):
        if s[i][j] == '.': c += 1
        else: c = 0
        yoko[i][j] = c
    for k in range(w-1)[::-1]:
        if yoko[i][k] != 0 and yoko[i][k+1] != 0:
            yoko[i][k] = yoko[i][k+1]
for j in range(w):
    c = 0
    for i in range(h):
        if s[i][j] == '.': c += 1
        else: c = 0
        tate[i][j] = c
    for k in range(h-1)[::-1]:
        if tate[k][j] != 0 and tate[k+1][j] != 0:
            tate[k][j] = tate[k+1][j]
for i in range(h):
    for j in range(w):
        if yoko[i][j] != 0 and tate[i][j] != 0:
            ans = max(yoko[i][j]+tate[i][j]-1, ans)
print(ans)