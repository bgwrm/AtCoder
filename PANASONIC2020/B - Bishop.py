import math
h, w = (int(_) for _ in input().split())

if h == 1 or w == 1:
    print(1)
    exit()

print(math.ceil(h * w / 2))