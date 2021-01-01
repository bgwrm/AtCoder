n, m = (int(_) for _ in input().split())
a = [input() for _ in range(n)]
b = [input() for _ in range(m)]

for i in range(n-m+1):
    for j in range(n-m+1):
        sub = ['']*m
        for k in range(m):
            sub[k] = a[i+k][j:j+m]
        if sub == b:
            print('Yes')
            exit()
print('No')