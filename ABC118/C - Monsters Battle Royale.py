import math
n = int(input())
a = [int(_) for _ in input().split()]
ans = a[0]
for i in a:
    ans = math.gcd(ans, i)
print(ans)