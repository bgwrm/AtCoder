n, m = (int(_) for _ in input().split())
l1, l2 = [], []

for i in range(m):
    a, b = (int(_) for _ in input().split())
    if a == 1:
        l1 += [b]
    elif a == n:
        l2 += [b]
    elif b == 1:
        l1 += [a]
    elif b == n:
        l2 += [a]

if len(set(l1)&set(l2)) > 0:
    print('POSSIBLE')
else:
    print('IMPOSSIBLE')