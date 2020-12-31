n, t = (int(_) for _ in input().split())
a = [int(input()) for _ in range(n)]
a += [a[n-1]+t]
ans = 0

for i in range(n):
    ans += min(a[i+1], a[i]+t) - a[i]

print(ans)