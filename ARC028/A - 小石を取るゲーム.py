n, a, b = (int(_) for _ in input().split())
for i in range(10**4):
    if i%2==0:
        n -= a
    else:
        n -= b
    if n <= 0:
        print('Ant' if i%2 == 0 else 'Bug')
        exit()