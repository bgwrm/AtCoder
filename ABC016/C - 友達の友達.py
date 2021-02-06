n, m = (int(_) for _ in input().split())
l = [[] for _ in range(n)]
for i in range(m):
    a, b = (int(_) for _ in input().split())
    l[b-1] += [a-1]
    l[a-1] += [b-1]
for i in range(n):
    f, p, s = set(l[i]), set([i]), set()
    for j in f:
        s |= set(l[j])
    print(len(s-f-p))