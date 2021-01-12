n, k = (int(_) for _ in input().split())
a = [int(input()) for _ in range(n)]
now = 0
for i in range(n):
    now += a[i]
    if now >= k:
        print(i+1)
        exit()