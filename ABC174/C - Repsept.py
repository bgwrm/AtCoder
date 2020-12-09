k = int(input())
r = 0

if k % 2 == 0 or k % 5 == 0:
    print(-1)
    exit()

for i in range(k):
    r += 7 * pow(10, i, k)
    if r % k == 0:
        print(i+1)
        exit()