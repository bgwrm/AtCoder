import math
n = int(input())

x =  math.ceil(100 * n / 108)

if x * 1.08 // 1 != n:
    print(':(')
else:
    print(x)