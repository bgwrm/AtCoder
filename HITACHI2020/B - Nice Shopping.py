a, b, m = (int(_) for _ in input().split())
al = [int(_) for _ in input().split()]
bl = [int(_) for _ in input().split()]
p = [min(al)+min(bl)]

for i in range(m):
    x, y, c = (int(_) for _ in input().split())
    p += [al[x-1]+bl[y-1]-c]

print(min(p))