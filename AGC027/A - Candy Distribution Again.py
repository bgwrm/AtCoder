n, x = (int(_) for _ in input().split())
a = sorted([int(_) for _ in input().split()])

for i in range(n):
    x -= a[i]
    if x < 0:
        print(i)
        exit()
print(n-1 if x > 0 else n)