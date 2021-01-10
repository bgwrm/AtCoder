n, w = (int(_) for _ in input().split())
l = [0]*(2*10**5+1)
now = 0
for i in range(n):
    s, t, p = (int(_) for _ in input().split())
    l[s] += p
    l[t] -= p
for i in l:
    now += i
    if now > w:
        print('No')
        exit()
print('Yes')