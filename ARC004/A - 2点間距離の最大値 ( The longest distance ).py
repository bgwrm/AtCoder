import math
n = int(input())
xy = [[int(_) for _ in input().split()] for i in range(n)]
ans = 0.0

for i in range(n-1):
    for j in range(i, n):
        ans = max(ans, math.sqrt((xy[i][0]-xy[j][0])**2 + (xy[i][1]-xy[j][1])**2))

print(ans)