n, a, b = (int(_) for _ in input().split())
print(n*b if n<=5 else (n-5)*a+5*b)