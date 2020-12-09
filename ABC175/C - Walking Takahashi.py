x, k, d = (int(_) for _ in input().split())
x = abs(x)

if x >= k * d:
    print(x - k * d)
    exit()

num = (x - d * (k % 2)) % (2 * d)
print(min(num, abs(num - 2 * d)))