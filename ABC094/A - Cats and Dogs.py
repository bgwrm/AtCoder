a, b, x = (int(_) for _ in input().split())
print('YES' if a <= x and (a+b) >= x else 'NO')