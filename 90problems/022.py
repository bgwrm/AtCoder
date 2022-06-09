import math
a, b, c = (int(_) for _ in input().split())
p = math.gcd(a, b)
p = math.gcd(p, c)
print(a//p+b//p+c//p-3)