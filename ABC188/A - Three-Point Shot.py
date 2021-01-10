p = [int(_) for _ in input().split()]
print('Yes' if max(p) < min(p)+3 else 'No')