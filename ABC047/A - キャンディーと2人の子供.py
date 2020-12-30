a, b, c = (int(_) for _ in input().split())
print('Yes' if a + b == c or b + c == a or c + a == b else 'No')