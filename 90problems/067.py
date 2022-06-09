def conv(x):
    x = int(x)
    if (x//9): return conv(x//9)+str(x%9)
    return str(x%9)

n, k = input().split()
for _ in range(int(k)):
    d = 0
    for i in range(len(n)):
        d += int(n[-i-1])*(8**i)
    n = conv(d).replace('8', '5')
print(n)