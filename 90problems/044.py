n, q = (int(_) for _ in input().split())
a = [int(_) for _ in input().split()]
s = 0
for _ in range(q):
    t, x, y = (int(_) for _ in input().split())
    if t == 1:
        a[(s+x-1)%n], a[(s+y-1)%n] = a[(s+y-1)%n], a[(s+x-1)%n]
    elif t == 2:
        s = (s-1)%n
    else:
        print(a[(s+x-1)%n])