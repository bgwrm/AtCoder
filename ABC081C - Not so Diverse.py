from collections import Counter
n, k = (int(_) for _ in input().split())
a = Counter([int(_) for _ in input().split()]).most_common()
num = 0

if len(a) <= k:
  print(0)
  exit()

for i in range(k):
  num += a[i][1]
print(n-num)