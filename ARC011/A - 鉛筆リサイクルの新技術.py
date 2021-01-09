m, n, N = (int(_) for _ in input().split())
ans = N
while N >= m:
    ans += N//m*n
    N = N//m*n+N%m
print(ans)