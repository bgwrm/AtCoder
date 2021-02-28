n = int(input())
ans = 10**10
for _ in range(n):
    a, p, x = (int(_) for _ in input().split())
    if x-a > 0:
        ans = min(ans, p)
print(-1 if ans == 10**10 else ans)