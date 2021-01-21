n, m = (int(_) for _ in input().split())
red = [1] + [0]*(n-1)
num = [1]*n
for i in range(m):
    x, y = (int(_) for _ in input().split())
    num[x-1] -= 1
    num[y-1] += 1
    if red[x-1] == 1:
        red[y-1] = 1
    if num[x-1] == 0:
        red[x-1] = 0
print(sum(red))