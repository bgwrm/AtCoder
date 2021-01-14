n, m = (int(_) for _ in input().split())
a = sorted([int(_) for _ in input().split()], reverse=True)
b = sorted([int(_) for _ in input().split()], reverse=True)
if n < m:
    print('NO')
    exit()
for i in range(m):
    if a[i] < b[i]:
        print('NO')
        exit()
print('YES')