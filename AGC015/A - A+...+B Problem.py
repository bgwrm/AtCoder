from math import factorial
n, a, b = (int(_) for _ in input().split())

if a > b or (n == 1 and a != b):
    print(0)
elif n == 1 and a == b:
    print(1)
else:
    print((b-a)*(n-2)+1)