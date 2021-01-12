x, y = (int(_) for _ in input().split())
n = 1
if x%y == 0:
    print(-1)
    exit()
while n*x <= 10**18:
    if (n*x)%y != 0:
        print(n*x)
        exit()
    n += 1
print(-1)