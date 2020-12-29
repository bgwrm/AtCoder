n = int(input())
d = sorted([int(_) for _ in input().split()])
print(d[n//2] - d[n//2-1])