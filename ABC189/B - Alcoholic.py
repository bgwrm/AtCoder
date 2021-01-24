n, x = (int(_) for _ in input().split())
now = 0
for i in range(n):
    v, p = (int(_) for _ in input().split())
    now += v*p
    if now > x*100:
        print(i+1)
        exit()
print(-1)