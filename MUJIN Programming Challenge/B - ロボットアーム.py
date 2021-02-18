import math
l = [int(_) for _ in input().split()]
print((sum(l)**2-max(0, 2*max(l)-sum(l))**2)*math.pi)