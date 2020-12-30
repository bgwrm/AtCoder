a, b, c, d = (int(_) for _ in input().split())
print('Yes' if abs(a-c) <= d or (abs(a-b) <= d and abs(b-c) <= d) else 'No')