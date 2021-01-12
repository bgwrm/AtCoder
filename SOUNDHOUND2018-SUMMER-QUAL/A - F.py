a, b = (int(_) for _ in input().split())
print('+' if a+b == 15 else '*' if a*b == 15 else 'x')