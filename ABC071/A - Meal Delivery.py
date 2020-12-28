x, a, b = (int(_) for _ in input().split())
print('A' if abs(x - a) < abs(x - b) else 'B')