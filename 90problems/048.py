n, k = (int(_) for _ in input().split())
ab = [[int(_) for _ in input().split()] for i in range(n)]
ans, l = 0, []
for a, b in ab: l += [a-b, b]
print(sum(sorted(l, reverse=True)[:k]))