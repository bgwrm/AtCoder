n = int(input())
p = [[int(_) for _ in input().split()] for i in range(n)]
ans = 0
for i in p:
    ans = max(ans, sum(i[0:4])+i[4]*110/900)
print(ans)