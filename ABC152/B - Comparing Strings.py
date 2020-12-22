a, b = (int(_) for _ in input().split())
print(str(a)*b if a<=b else str(b)*a)