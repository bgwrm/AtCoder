from decimal import Decimal
import math
x, y, r = (Decimal(_) for _ in input().split())
ans = 0
x_start, x_end = math.ceil(x-r), math.floor(x+r)
for i in range(x_start, x_end+1):
    if r**2-(x-i)**2 >= 0:
        dy = (r**2-(x-i)**2).sqrt()
        ans += math.floor(y+dy)-math.ceil(y-dy)+1
print(ans)