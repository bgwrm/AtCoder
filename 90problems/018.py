import math
t = int(input())
l, x, y = (int(_) for _ in input().split())
for _ in range(int(input())):
    e = int(input())
    dy = y+l*math.sin(math.radians(360)*e/t)/2
    z = l/2-l*math.cos(math.radians(360)*e/t)/2
    print(math.degrees(math.atan2(z, (x*x+dy*dy)**0.5)))