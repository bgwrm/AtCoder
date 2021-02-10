import itertools
n = int(input())
ans, l = 0, []
for i in range(n):
    a = int(input())
    for j in range(a):
        x, y = (int(_) for _ in input().split())
        l += [[i, x-1, y]]
for p in itertools.product([0, 1], repeat=n):
    for i, x, y in l:
        if p[i] == 1 and p[x] != y:
            break
    else:
        ans = max(sum(p), ans)
print(ans)