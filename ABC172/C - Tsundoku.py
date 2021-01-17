import bisect
n, m, k = (int(_) for _ in input().split())
a = [0]+[int(_) for _ in input().split()]
b = [int(_) for _ in input().split()]
ans = 0
for i in range(1,n+1):
    a[i] = a[i]+a[i-1]
for i in range(1,m):
    b[i] = b[i]+b[i-1]
for i in range(n+1):
    t = k-a[i]
    if t < 0:
        break
    ans = max(i+bisect.bisect(b,t), ans)
print(ans)