a, b = (int(_) for _ in input().split())
print('Ant' if abs(a) < abs(b) else 'Bug' if abs(a) > abs(b) else 'Draw')