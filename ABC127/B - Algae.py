r, d, x = (int(_) for _ in input().split())
for i in range(10):
    x = r * x - d
    print(x)