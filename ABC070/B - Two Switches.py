a, b, c, d = (int(_) for _ in input().split())
print(max(min(b,d)-max(a,c), 0))