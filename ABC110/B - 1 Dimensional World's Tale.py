n, m, x, y = (int(_) for _ in input().split())
x_max = max([int(_) for _ in input().split()]+[x])
y_min = min([int(_) for _ in input().split()]+[y])
print('War' if x_max >= y_min else 'No War')