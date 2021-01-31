n, s, d = (int(_) for _ in input().split())
for i in range(n):
    x, y = (int(_) for _ in input().split())
    if x < s and y > d:
        print('Yes')
        exit()
print('No')