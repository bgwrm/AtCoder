from math import sqrt
n = int(input())
xy = [[int(_) for _ in input().split()] for i in range(n)]
d = 0
w = 0

for i in range(n-1):
    for j in range(i+1, n):
        d += sqrt((xy[j][0]-xy[i][0])**2 + (xy[j][1]-xy[i][1])**2)
        w += 1

print(d*(n-1)/w)