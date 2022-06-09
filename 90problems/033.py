import math
h, w = (int(_) for _ in input().split())
print(h*w if h == 1 or w == 1 else math.ceil(h/2)*math.ceil(w/2))