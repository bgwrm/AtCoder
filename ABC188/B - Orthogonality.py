n = int(input())
a = [int(_) for _ in input().split()]
b = [int(_) for _ in input().split()]
t = 0
for i in range(n):
    t += a[i]*b[i]
print('Yes' if t == 0 else 'No')