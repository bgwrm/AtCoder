se = [[int(_) for _ in input().split()] for i in range(3)]
ans = 0
for i in se:
    ans += i[0] * i[1] // 10
print(ans)