n, k = (int(_) for _ in input().split())
h = sorted([int(_) for _ in input().split()])

if k == 0:
    print(sum(h))
else:
    print(sum(h)-sum(h[-k:]))