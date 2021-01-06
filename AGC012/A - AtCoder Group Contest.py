n = int(input())
a = sorted([int(_) for _ in input().split()])
print(sum(a[n::2]))