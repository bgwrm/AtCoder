n, q = (int(_) for _ in input().split())
a = [0] * n

for _ in range(q):
    l, r, t = (int(_) for _ in input().split())
    for i in range(l-1, r):
        a[i] = t

for i in a:
    print(i)