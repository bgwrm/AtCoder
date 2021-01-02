n = int(input())
xy = [[int(_) for _ in input().split()] for i in range(n)]
ans = 0

for i in range(n):
    for j in range(i+1,n):
        dx = abs(xy[i][0]-xy[j][0])
        dy = abs(xy[i][1]-xy[j][1])
        if dy / dx <= 1:
            ans += 1

print(ans)