h, w = (int(_) for _ in input().split())
l = [list(input()) for _ in range(h)]
ans = b = 0
for i in range(h):
    for j in range(w):
        c = 0
        if l[i][j] == '#':
            b += 1
        if i == 0 or i == h-1 or j == 0 or j == w-1:
            continue
        if l[i-1][j] != l[i][j]:
            c += 1
        if l[i][j-1] != l[i][j]:
            c += 1
        if l[i+1][j] != l[i][j]:
            c += 1
        if l[i][j+1] != l[i][j]:
            c += 1
        if c == 2 and l[i-1][j] != l[i+1][j] and l[i][j-1] != l[i][j+1]:
            ans += 1
        elif c == 3:
            ans += 2
print(ans if b > 1 else 4)