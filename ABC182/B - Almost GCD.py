n = int(input())
a = [int(x) for x in input().split()]
max = 0
ans = 0

for i in range(2, 1001):
  count = 0
  for j in range(n):
    if a[j] % i == 0:
      count += 1
  if count > max:
    max = count
    ans = i

print(ans)