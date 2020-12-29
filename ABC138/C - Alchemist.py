n = int(input())
v = sorted([int(_) for _ in input().split()])
ans = v[0]

for i in range(1, n):
    ans = (ans + v[i]) / 2

print(ans)