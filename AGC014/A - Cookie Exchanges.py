a, b, c = (int(_) for _ in input().split())

for i in range(10**9):
    if sum(num%2 for num in [a, b, c]) > 0:
        print(i)
        break
    if a == b == c:
        print(-1)
        break
    a, b, c = (b+c)/2, (a+c)/2, (a+b)/2