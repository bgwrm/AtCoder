n, m = (int(_) for _ in input().split())
ab = [[int(_) for _ in input().split()] for i in range(m)]
ans = [0] * n

for i in ab:
    ans[i[0] - 1] += 1
    ans[i[1] - 1] += 1

for i in ans:
    print(i)