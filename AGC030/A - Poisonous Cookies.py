a, b, c = (int(_) for _ in input().split())
if a+b+1 >= c:
    print(b+c)
else:
    print(a+2*b+1)