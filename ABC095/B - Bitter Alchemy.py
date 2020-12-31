n, x = (int(_) for _ in input().split())
m = sorted([int(input()) for _ in range(n)])
x -= sum(m)
print(n+x//m[0])