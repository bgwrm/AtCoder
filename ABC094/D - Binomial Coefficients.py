n = int(input())
a = [int(_) for _ in input().split()]
ma = max(a)
if n == 2:
    print(ma, min(a))
else:
    print(ma, min(a, key=lambda x:abs(x-ma/2)))