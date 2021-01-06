n = int(input())
a = [int(_) for _ in input().split()]
c = 0
for i in range(n):
    if i+1 == a[a[i]-1]:
        c += 1
print(c//2)