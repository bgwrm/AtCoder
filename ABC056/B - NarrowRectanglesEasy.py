w, a, b = (int(_) for _ in input().split())
print(0 if (a <= b and b <= a+w) or (a <= b+w and b+w <= a+w) else min(abs(b-a-w), abs(a-b-w)))