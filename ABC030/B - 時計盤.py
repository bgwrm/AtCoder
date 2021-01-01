n, m = (int(_) for _ in input().split())
print(min(abs(30*(n%12)-5.5*m),360-abs(30*(n%12)-5.5*m)))