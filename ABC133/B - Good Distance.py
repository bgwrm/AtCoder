import math
n, d = (int(_) for _ in input().split())
x = [[int(_) for _ in input().split()] for i in range(n)]
ans = 0

for i in range(n-1):
    for j in range(i+1, n):
        d2 = 0
        for k in range(d):
            d2 += (x[i][k] - x[j][k])**2
        if float.is_integer(math.sqrt(d2)):
            ans += 1

print(ans)