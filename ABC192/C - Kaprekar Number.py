n, k = (int(_) for _ in input().split())
l = [str(n)]
for _ in range(k):
    g1 = int(''.join(sorted(str(l[-1]),reverse=True)))
    g2 = int(''.join(sorted(str(l[-1]))))
    l += [g1-g2]
print(l[-1])