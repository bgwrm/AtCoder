n, k = (int(_) for _ in input().split())
ans = 1
for i in range(k, n+1):
    ans += i*n-(i-1)*i+1
    ans %= 10**9+7
print(ans)