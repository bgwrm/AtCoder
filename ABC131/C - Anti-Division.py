import math

def lcm(x, y):
    return (x * y) // math.gcd(x, y)

a, b, c, d = (int(_) for _ in input().split())
n = lcm(c,d)
print(b - a + 1 - b//c - b//d + b//n + (a-1)//c + (a-1)//d - (a-1)//n)