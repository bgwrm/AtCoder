n, m, x = (int(_) for _ in input().split())
a = [int(_) for _ in input().split()]
c1, c2 = 0, 0
for i in a:
    if i < x:
        c1 += 1
    else:
        c2 += 1
print(min(c1,c2))