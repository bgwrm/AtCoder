na, nb = (int(_) for _ in input().split())
a = set([int(_) for _ in input().split()])
b = set([int(_) for _ in input().split()])
print(len(a&b)/len(a|b))