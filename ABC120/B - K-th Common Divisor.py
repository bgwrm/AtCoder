a, b, k = (int(_) for _ in input().split())
count = 0

for i in range(100, 0, -1):
    if a%i == 0 and b%i == 0:
        count += 1
        if k == count:
            print(i)
            exit()