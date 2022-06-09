n = int(input())
ans, mod = 1, 10**9+7
for _ in range(n):
    ans = (ans*sum([int(_) for _ in input().split()]))%mod
print(ans)