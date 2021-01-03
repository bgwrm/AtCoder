s = input()
n = int(input())
a, b = (int(_) for _ in input().split())
x = [int(_) for _ in input().split()]
l = [input() for _ in range(n)]
xy = [[int(_) for _ in input().split()] for i in range(n)]
mod = 10 ** 9 + 7

# Yes/No出力
print('Yes' if n%2 == 0 else 'No')
print('No' if n%2 == 0 else 'Yes')

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

# 約数のリスト
small = []
big = []
i = 2
while i * i <= n:
    if n % i == 0:
        small.append(i)
        if i != n // i:
            big.append(n // i)
    i += 1
numlist = small + big[::-1]

# 組み合わせリスト
import itertools
com = list(itertools.combinations(l,2))

# 重複可全列挙
com = list(itertools.product(l, repeat=2))

# 出現数カウント
from collections import Counter
c = Counter(l)
print(c['s']) # sの出現回数
print(c.items()) # アイテム名と出現回数のタプル
print(c.most_common()) # 出現回数多い順

# 素数判定
def is_prime(num):
    if num < 2:
        return False
    elif num == 2:
        return True
    elif num % 2 == 0:
        return False
    for i in range(3, num + 1, 2):
        if i * i > num:
            break
        if num % i == 0:
            return False
    return True

# アルファベットのリスト
print([chr(ord("a")+i) for i in range(26)])

# 2で何回割り切れるか
print(format(n, 'b')[::-1].find('1'))

# 10進数 -> 2進数、8進数、16進数
bin_str = format(n, 'b')
oct_str = format(n, 'o')
hex_str = format(n, 'x')

# リスト読み込みと同時に添え字(_i)もつける
l = [(int(_), i) for i, _ in enumerate(input().split(), 1)]

# 優先度付きキュー
# 計算量O(logN)で最小値を取り出せる
# 最大値で使いたい場合は予め-1を掛けておく
import heapq
heapq.heapify(l) # リストを優先度付きキューに変換
heapq.heappop(l) # 最小値を取り出す
heapq.heappush(l, n) # 要素を挿入

# bit全探索
# (i>>j)&1 iをjbitずらした数が1ならばTrue
for i in range(2**n):
    a = 0
    for j in range(n):
        if (i>>j)&1:
            a += l[j]