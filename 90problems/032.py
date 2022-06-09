import itertools
n = int(input())
a = [[int(_) for _ in input().split()] for i in range(n)]
l = [[] for _ in range(n)]
ans = 10**6
for _ in range(int(input())):
    x, y = (int(_) for _ in input().split())
    l[x-1] += [y-1]
    l[y-1] += [x-1]
for per in list(itertools.permutations(range(n), n)):
    t = 0
    for i in range(n):
        if i != 0 and per[i-1] in l[per[i]]: break
        t += a[per[i]][i]
    else:
        ans = min(ans, t)
print(-1 if ans == 10**6 else ans)