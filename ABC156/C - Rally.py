n = int(input())
x = [int(_) for _ in input().split()]
ans = 10000000

for i in range(100):
    sum = 0
    for xi in x:
        sum += (xi-i+1)**2
    if sum < ans:
        ans = sum

print(ans)