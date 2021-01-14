n, a, b = (int(_) for _ in input().split())
l = [int(input()) for _ in range(n)]
if len(set(l)) == 1:
    print(-1)
else:
    p = b/(max(l)-min(l))
    q = a-sum(l)*p/n
    print(p, q)