import math
a, b = (int(_) for _ in input().split())
print(a*b//math.gcd(a,b))