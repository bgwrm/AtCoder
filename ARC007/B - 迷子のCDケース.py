n, m = (int(_) for _ in input().split())
d = [int(input()) for _ in range(m)]
l = [int(_) for _ in range(1,n+1)]
now = 0
for i in d:
    if now == i:
        continue
    l[l.index(i)] = now
    now = i
for i in l:
    print(i)