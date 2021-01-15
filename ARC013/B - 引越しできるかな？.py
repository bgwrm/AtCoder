c = int(input())
x = y = z = 0
for i in range(c):
    l = sorted([int(_) for _ in input().split()])
    x, y, z = max(l[0], x), max(l[1], y), max(l[2], z)
print(x*y*z)