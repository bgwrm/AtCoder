s = input()
n = int(input())
a, b = (int(_) for _ in input().split())
x = [int(_) for _ in input().split()]
l = [input() for _ in range(n)]
xy = [[int(_) for _ in input().split()] for i in range(n)]
mod = 10 ** 9 + 7

# ソート
s.sort()
s = sorted(s)

# 最大公約数
import math
x = 0
y = 0
math.gcd(x, y)

# 最小公倍数
def lcm(x, y):
    return (x * y) // math.gcd(x, y)

# 組み合わせリスト
import itertools
com = list(itertools.combinations(l,2))

# 出現数カウント
from collections import Counter
c = Counter(l)
print(c('s')) # sの出現回数
print(c.most_common()) # 出現回数多い順