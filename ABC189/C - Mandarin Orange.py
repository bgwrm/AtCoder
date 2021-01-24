n = int(input())
a = [int(_) for _ in input().split()]
ans = 0
for i in range(n):
    c = 10**6
    for j in range(i,n):
        c = min(a[j], c)
        ans = max(c*(j-i+1), ans)
print(ans)