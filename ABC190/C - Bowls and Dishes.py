n, m = (int(_) for _ in input().split())
ab = [[int(_) for _ in input().split()] for i in range(m)]
k = int(input())
cd = [[int(_) for _ in input().split()] for i in range(k)]
ans = 0
for i in range(2**k):
    dish = [0]*n
    for j in range(k):
        if (i>>j)&1:
            dish[cd[j][1]-1] += 1
        else:
            dish[cd[j][0]-1] += 1
    c = 0
    for l in range(m):
        if dish[ab[l][0]-1] > 0 and dish[ab[l][1]-1] > 0:
            c += 1
    ans = max(c, ans)
print(ans)