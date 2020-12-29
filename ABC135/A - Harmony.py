a, b = (int(_) for _ in input().split())
print(max(a, b) - abs(a-b)//2 if abs(a-b)%2 == 0 else 'IMPOSSIBLE')