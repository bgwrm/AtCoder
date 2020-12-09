N = int(input())
A = [int(x) for x in input().split()]
ans = 10**9

for i in range(N):
  min = format(A[i], 'b')[::-1].find('1')
  if ans > min:
    ans = min

print(ans)