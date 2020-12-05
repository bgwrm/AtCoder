import itertools

n, k = (int(_) for _ in input().split())
t = [[int(_) for _ in input().split()] for i in range(n)]
rp = list(itertools.permutations(range(1, n)))
ans = 0

for i in range(len(rp)):
  now = 0
  tsum = 0
  for j in range(n-1):
    tsum += t[now][rp[i][j]]
    now = rp[i][j]
  tsum += t[now][0]
  if k == tsum:
    ans += 1

print(ans)