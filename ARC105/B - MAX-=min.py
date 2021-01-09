import math
n = int(input())
a = [int(_) for _ in input().split()]
ans = a[0]
for i in range(1,n):
    ans = math.gcd(ans,a[i])
print(ans)