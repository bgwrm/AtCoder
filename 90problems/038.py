import math
a, b = (int(_) for _ in input().split())
g = (a*b)//math.gcd(a, b)
print(g if g <= 10**18 else 'Large')