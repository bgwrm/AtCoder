import math
a, b, k, l = (int(_) for _ in input().split())
print(min(a*k, k//l*b+k%l*a, math.ceil(k/l)*b))