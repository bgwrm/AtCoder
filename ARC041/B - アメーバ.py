n, m = (int(_) for _ in input().split())
b = [list(map(int, str(input()))) for i in range(n)]
a = [['0']*m for _ in range(n)]
for i in range(1, n-1):
    for j in range(1, m-1):
        c = min(b[i-1][j], b[i+1][j], b[i][j-1], b[i][j+1])
        b[i-1][j] -= c
        b[i+1][j] -= c
        b[i][j-1] -= c
        b[i][j+1] -= c
        a[i][j] = str(c)
for i in range(n):
    print(''.join(a[i]))