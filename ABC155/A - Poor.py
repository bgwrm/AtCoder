a, b, c = (int(_) for _ in input().split())
if (a == b and a != c) or (a == c and a != b) or (b == c and a!= b):
    print('Yes')
else:
    print('No')