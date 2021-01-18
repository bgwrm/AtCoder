n, m = (int(_) for _ in input().split())
print(pow(10, n, m*m)//m%m)