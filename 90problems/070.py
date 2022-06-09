n = int(input())
xy = [[int(_) for _ in input().split()] for i in range(n)]
x, y = [sorted(list(i)) for i in zip(*xy)]
ans, a, b = 0, x[n//2], y[n//2]
if n > 1:
    for i in range(n): ans += abs(x[i]-a)+abs(y[i]-b)
print(ans)