n = int(input())
mt = [[float(_) for _ in input().split()] for i in range(n)]
ans = [0] * 6

for t in mt:
    if t[0] >= 35:
        ans[0] += 1
    if t[0] >= 30 and t[0] < 35:
        ans[1] += 1
    if t[0] >= 25 and t[0] < 30:
        ans[2] += 1
    if t[1] >= 25:
        ans[3] += 1
    if t[1] < 0 and t[0] >= 0:
        ans[4] += 1
    if t[0] < 0:
        ans[5] += 1

print(' '.join(str(_) for _ in ans))