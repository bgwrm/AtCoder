a, b = (int(_) for _ in input().split())
print(b if a > 12 else b//2 if a >= 6 else 0)