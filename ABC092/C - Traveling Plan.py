n = int(input())
a = [0] + [int(_) for _ in input().split()] + [0]
all = 0

for i in range(len(a)-1):
    all += abs(a[i+1] - a[i])

for i in range(n):
    print(all - abs(a[i+1] - a[i]) - abs(a[i+2] - a[i+1]) + abs(a[i+2] - a[i]))