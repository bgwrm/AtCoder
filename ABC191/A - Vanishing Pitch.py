v, t, s, d = (int(_) for _ in input().split())
print('No' if v*t <= d <= v*s else 'Yes')