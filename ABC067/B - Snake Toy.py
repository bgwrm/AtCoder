n, k = (int(_) for _ in input().split())
l = sorted([int(_) for _ in input().split()], reverse=True)
print(sum(l[:k]))