import math
n = int(input())
a = [int(_) for _ in input().split()]
print(math.ceil(sum(a)/(n-a.count(0))))