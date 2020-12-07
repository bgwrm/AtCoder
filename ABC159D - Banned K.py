import collections

n = int(input())
a = [int(_) for _ in input().split()]
c = collections.Counter(a)
sum = 0

for i in c:
    sum += c[i]*(c[i]-1)//2

for i in range(n):
    print(sum-c[a[i]]+1)