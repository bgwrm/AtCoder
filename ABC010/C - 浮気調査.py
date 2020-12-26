import math
txa, tya, txb, tyb, t, v = (int(_) for _ in input().split())
n = int(input())
xy = [[int(_) for _ in input().split()] for i in range(n)]

for p in xy:
    if math.sqrt((p[0]-txa)**2 + (p[1]-tya)**2) + math.sqrt((p[0]-txb)**2 + (p[1]-tyb)**2) <= v * t:
        print('YES')
        exit()

print('NO')