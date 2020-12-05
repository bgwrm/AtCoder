n = int(input())
ab = [[int(x) for x in input().split()] for y in range(n)]
ans = 0

for i in range(n):
    num = ab[i][1] - ab[i][0]
    ans += (num + 1) * ab[i][0] + (num * num + num) // 2

print(ans)