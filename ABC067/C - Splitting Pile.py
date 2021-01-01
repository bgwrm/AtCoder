n = int(input())
a = [int(_) for _ in input().split()]
t, s = sum(a), 0
l = []
for i in range(n-1):
    s += a[i]
    l += [abs(2*s-t)]
print(min(l))