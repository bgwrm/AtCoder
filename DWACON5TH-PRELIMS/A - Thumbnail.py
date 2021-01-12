n = int(input())
a = [int(_) for _ in input().split()]
ans, t, m =0, sum(a), 10**6
for i in range(n):
    if abs(t-n*a[i]) < m:
        m = abs(t-n*a[i])
        ans = i
print(ans)