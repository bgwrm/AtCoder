n, x = (int(_) for _ in input().split())
a = [int(_) for _ in input().split()]
ans = []
for i in a:
    if i != x:
        ans += [i]
print(*ans)