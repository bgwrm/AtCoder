import math
n, x = (int(_) for _ in input().split())
xs = [int(_) for _ in input().split()]
diff = [abs(_ - x) for _ in xs]
ans = 10**9

if n == 1:
    print(diff[0])
else:
    for i in range(n-1):
        ans = min(ans, math.gcd(diff[i], diff[i+1]))
    print(ans)