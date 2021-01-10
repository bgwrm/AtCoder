n, a, b, l = (int(_) for _ in input().split())
for i in range(n):
    l *= b/a
print('{:.12f}'.format(l))