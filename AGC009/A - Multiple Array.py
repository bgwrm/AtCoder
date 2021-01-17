n = int(input())
ab = [[int(_) for _ in input().split()] for i in range(n)][::-1]
ans = 0
for a, b in ab:
    if (a+ans)%b != 0:
        ans += b-(a+ans)%b
print(ans)