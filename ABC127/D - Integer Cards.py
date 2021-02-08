n, m = (int(_) for _ in input().split())
a = [int(_) for _ in input().split()]
bc = sorted([[int(_) for _ in input().split()] for i in range(m)], key=lambda x:-x[1])
l = []
for b, c in bc:
    a += [c]*b
    if len(a) > 2*n:
        break
a = sorted(a, reverse=True)
print(sum(a[:n]))