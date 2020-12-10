n, m = (int(_) for _ in input().split())
ab = [[int(_) for _ in input().split()] for i in range(n)]
cd = [[int(_) for _ in input().split()] for i in range(m)]

for i in range(n):
    dist = [0] * m
    for j in range(m):
        dist[j] = abs(ab[i][0] - cd[j][0]) + abs(ab[i][1] - cd[j][1])
    print(dist.index(min(dist)) + 1)