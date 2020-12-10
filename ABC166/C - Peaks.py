n, m = (int(_) for _ in input().split())
h = [int(_) for _ in input().split()]
ab = [[int(_) for _ in input().split()] for i in range(m)]
bad = set()

for i in ab:
    if h[i[0] - 1] >= h[i[1] -1]:
        bad.add(i[1])
    if h[i[0] - 1] <= h[i[1] -1]:
        bad.add(i[0])

print(n-len(bad))