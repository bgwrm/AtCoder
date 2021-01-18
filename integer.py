n, a, b = 0, 0, 0

# 最大公約数
import math
math.gcd(a, b)

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

# 整数判定
f = 2.0
print(f.is_integer()) # True

# 2で何回割り切れるか
print(format(n, 'b')[::-1].find('1'))

# 10進数 -> 2進数、8進数、16進数
bin_str = format(n, 'b')
oct_str = format(n, 'o')
hex_str = format(n, 'x')

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