n, m = (int(_) for _ in input().split())
ans, c, l = ['']*m, [0]*n, []
for i in range(m):
    p, y = (int(_) for _ in input().split())
    l += [[y, p, i]]
l = sorted(l)
for y, p, i in l:
    c[p-1] += 1
    ans[i] = str(p).zfill(6)+str(c[p-1]).zfill(6)
print(*ans, sep='\n')