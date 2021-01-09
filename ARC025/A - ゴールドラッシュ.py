d = [int(_) for _ in input().split()]
j = [int(_) for _ in input().split()]
ans = 0
for i in range(7):
    ans += max(d[i],j[i])
print(ans)