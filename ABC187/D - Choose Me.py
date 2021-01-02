n = int(input())
ab = [[int(_) for _ in input().split()] for i in range(n)]
sum_a, t, ans = 0, 0, 0
l = []

for i in range(n):
    l += [[2*ab[i][0]+ab[i][1], ab[i][0], ab[i][1]]]
    sum_a += ab[i][0]
l = sorted(l, reverse=True)

for i in l:
    t += i[1] + i[2]
    sum_a -= i[1]
    ans += 1
    if sum_a < t:
        print(ans)
        exit()