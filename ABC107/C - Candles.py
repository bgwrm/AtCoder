n, k = (int(_) for _ in input().split())
x = [int(_) for _ in input().split()]
ans = 10**9
for i in range(n-k+1):
    d = abs(x[i+k-1]-x[i]) + min(abs(x[i+k-1]), abs(x[i]))
    ans = min(d, ans)
print(ans)