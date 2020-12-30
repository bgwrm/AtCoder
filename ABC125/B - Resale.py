n = int(input())
v = [int(_) for _ in input().split()]
c = [int(_) for _ in input().split()]
ans = 0

for i in range(n):
    if v[i] > c[i]:
        ans += v[i] - c[i]

print(ans)