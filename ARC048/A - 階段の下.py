a, b = (int(_) for _ in input().split())
n = 1 if a < 0 and b > 0 else 0
print(b-a-n)