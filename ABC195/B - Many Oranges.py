import math
a, b, w = (int(_) for _ in input().split())
v = [math.ceil(w*1000/b), int(w*1000/a)]
if v[0] > v[1]:
    print('UNSATISFIABLE')
else:
    print(*v)