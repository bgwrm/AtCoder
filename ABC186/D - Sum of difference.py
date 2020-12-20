n = int(input())
a = sorted([int(_) for _ in input().split()])
m = a[0]
ans = 0
 
for i in range(n-1):
    ans += a[i+1]*(i+1) - m
    m += a[i+1]

print(ans)