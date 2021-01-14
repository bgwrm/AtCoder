n = int(input())
a = [int(_) for _ in input().split()]
l = [0, abs(a[1]-a[0])]
for i in range(2, n):
    l += [min(l[i-2]+abs(a[i]-a[i-2]), l[i-1]+abs(a[i]-a[i-1]))]
print(l[-1])