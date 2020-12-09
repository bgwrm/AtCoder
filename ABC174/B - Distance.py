n,d = (int(_) for _ in input().split())
xy = [[int(_) for _ in input().split()] for n in range(n)]
ans = 0

for i in range(n):
    if d**2 >= xy[i][0]**2 + xy[i][1]**2:
        ans += 1

print(ans)