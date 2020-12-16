s = input()
n = int(input())
a, b = (int(_) for _ in input().split())
s = [int(_) for _ in input().split()]
xy = [[int(_) for _ in input().split()] for i in range(n)]
mod = 10 ** 9 + 7

# 最大公約数
import math
math.gcd(x, y)

# 最小公倍数
def lcm(x, y):
    return (x * y) // math.gcd(x, y)