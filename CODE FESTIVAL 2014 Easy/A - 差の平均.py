n = int(input())
a = [int(_) for _ in input().split()]
total = 0
for i in range(n-1):
    total += a[i+1] - a[i]
print(total/(n-1))