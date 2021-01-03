t = int(input())
n = int(input())
a = [int(_) for _ in input().split()]
m = int(input())
b = [int(_) for _ in input().split()]
ans = 0

for i in b:
    for j in range(len(a)):
        if a[j] + t >= i and a[j] <= i:
            del a[j]
            ans += 1
            break

print('yes' if ans == m else 'no')