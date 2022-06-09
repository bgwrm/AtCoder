n = int(input())
a = [int(_) for _ in input().split()]*2
now, s, l = 0, sum(a)//2, 0
if s%10 != 0: exit(print('No'))
s //= 10
for i in range(n):
    while now < s:
        now += a[l]
        l += 1
    if now == s: exit(print('Yes'))
    now -= a[i]
print('No')