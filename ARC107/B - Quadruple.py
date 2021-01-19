n, k = (abs(int(_)) for _ in input().split())
x = [0]*(2*n+1)
ans = 0
for i in range(2, 2*n+1):
    x[i] = min(i-1, 2*n+1-i)
for i in range(k, 2*n+1):
    ans += x[i]*x[i-k]
print(ans)