n = int(input())
a = sorted([int(_) for _ in input().split()])
b = sorted([int(_) for _ in input().split()])
print(sum([abs(a[i]-b[i]) for i in range(n)]))