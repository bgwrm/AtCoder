n = int(input())
a = [int(_) for _ in input().split()]
m = 1000
for i in range(n-1):
    m += max(m//a[i]*(a[i+1]-a[i]), 0)
print(m)