import math
x1, y1, r = (int(_) for _ in input().split())
x2, y2, x3, y3 = (int(_) for _ in input().split())
if x1+r<=x3 and x1-r>=x2 and y1+r<=y3 and y1-r>=y2:
    print('NO')
else:
    print('YES')
if math.sqrt((x2-x1)**2+(y2-y1)**2)<=r and math.sqrt((x2-x1)**2+(y3-y1)**2)<=r and math.sqrt((x3-x1)**2+(y2-y1)**2)<=r and math.sqrt((x3-x1)**2+(y3-y1)**2)<=r:
    print('NO')
else:
    print('YES')