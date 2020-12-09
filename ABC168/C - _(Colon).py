import math
a, b, h, m = (int(_) for _ in input().split())
theta_a = (60 * h + m) * 0.5
theta_b = m * 6
theta = min(abs(theta_a - theta_b), 360 - abs(theta_a - theta_b))
print(math.sqrt(a**2 + b**2 - 2 * a * b * math.cos(math.radians(theta))))