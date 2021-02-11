import math
n, k = (int(_) for _ in input().split())
a = [int(_) for _ in input().split()]
g = a[0]
for i in a:
    g = math.gcd(g, i)
print('POSSIBLE' if k%g == 0 and k <= max(a) else 'IMPOSSIBLE')