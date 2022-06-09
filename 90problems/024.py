n, k = (int(_) for _ in input().split())
a = [int(_) for _ in input().split()]
b = [int(_) for _ in input().split()]
c = 0
for i in range(n):
    c += abs(a[i]-b[i])
print('No' if k < c or (k-c)%2 != 0 else 'Yes')