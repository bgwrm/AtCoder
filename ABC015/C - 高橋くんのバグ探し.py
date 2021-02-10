import itertools
n, k = (int(_) for _ in input().split())
t = [[int(_) for _ in input().split()] for i in range(n)]
for p in itertools.product(list(range(0, k)), repeat=n):
    r = t[0][p[0]]
    for i in range(1, n):
        r ^= t[i][p[i]]
    if r == 0:
        print('Found')
        exit()
print('Nothing')