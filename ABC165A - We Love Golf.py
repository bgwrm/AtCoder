k = int(input())
ab = [int(x) for x in input().split()]

for i in range(ab[1] - ab[0] + 1):
  if (i + ab[0]) % k == 0:
    print('OK')
    exit()

print('NG')