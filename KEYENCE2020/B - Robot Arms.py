n = int(input())
xl = sorted([[int(_) for _ in input().split()] for i in range(n)],key=sum)
p = -10**9
ans = 0
for i in range(n):
    if p <= xl[i][0]-xl[i][1]:
        ans += 1
        p = xl[i][0]+xl[i][1]
print(ans)