n, a, b = (int(_) for _ in input().split())
print('Alice' if (b-a)%2 == 0 else 'Borys')