a, b, c, k = (int(_) for _ in input().split())
s, t = (int(_) for _ in input().split())

print(a*s+b*t if (s+t)<k else a*s+b*t-(s+t)*c)