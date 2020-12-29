import math
n = int(input())
a = [int(_) for _ in input().split()]
num = 1
den = 0

for i in a:
    num = (num * i) // math.gcd(num, i)

for i in a:
    den += num / i

print(num / den)