n = int(input())
cp = [[int(_) for _ in input().split()] for i in range(n)]
q = int(input())
c1, c2 = [0], [0]
for i in range(n):
    c, p = cp[i]
    if c == 1:
        c1 += [c1[-1]+p]
        c2 += [c2[-1]]
    else:
        c1 += [c1[-1]]
        c2 += [c2[-1]+p]
for _ in range(q):
    l, r = (int(_) for _ in input().split())
    print(c1[r]-c1[l-1], c2[r]-c2[l-1])