n, m = (int(_) for _ in input().split())
x = sorted([int(_) for _ in input().split()])
diff = [0] * (m-1)

if m == 1:
    print(0)
    exit()

for i in range(m-1):
    diff[i] = x[i+1] - x[i]

print(sum(sorted(diff, reverse=True)[n-1:]))