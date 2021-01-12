n, a, b = (int(_) for _ in input().split())
print(min(a,b), max(a+b-n,0))