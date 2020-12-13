n, m, t = (int(_) for _ in input().split())
ab = [[int(_) for _ in input().split()] for i in range(m)]
max = n
now = 0

for i in range(m):
    n -= ab[i][0] - now
    if n <= 0:
        print('No')
        exit()
    n = min(n + ab[i][1] - ab[i][0], max)
    now = ab[i][1]

n -= t - now
if n <= 0:
    print('No')
    exit()

print('Yes')