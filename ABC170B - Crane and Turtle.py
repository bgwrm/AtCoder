x, y = (int(_) for _ in input().split())
print('Yes' if y%2 == 0 and y >= 2*x and y <= 4*x else 'No')