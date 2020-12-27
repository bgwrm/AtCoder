n = int(input())
a = sorted([int(_) for _ in input().split()])
print(a[-1] - a[0])