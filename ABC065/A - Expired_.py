x, a, b = (int(_) for _ in input().split())
print('delicious' if a >= b else 'safe' if a + x >= b else 'dangerous')