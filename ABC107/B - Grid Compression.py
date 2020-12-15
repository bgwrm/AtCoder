h, w = (int(_) for _ in input().split())
a = [list(input()) for i in range(h)]
row = [0] * h
col = [0] * w
r = 0

for i in range(h):
    for j in range(w):
        if a[i][j] == '#':
            row[i] += 1
            col[j] += 1

for i in range(h):
    c = 0
    if row[i] == 0:
        del a[i-r]
        r += 1
        continue
    for j in range(w):
        if col[j] == 0:
            del a[i-r][j-c]
            c += 1

for i in range(len(a)):
    print(''.join(a[i]))