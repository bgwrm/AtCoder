n = int(input())
l = sorted([int(_) for _ in input().split()])
print(sum(l[::2]))