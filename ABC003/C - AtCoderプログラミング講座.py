n, k = (int(_) for _ in input().split())
r = sorted([int(_) for _ in input().split()])
ans = 0

for i in r[-k:]:
    ans = (ans + i)/2

print(ans)