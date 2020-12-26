a = [int(_) for _ in input().split()]
print('win' if sum(a) <= 21 else 'bust')