n = int(input())
small = []
big = []
i = 1

while i * i <= n:
    if n % i == 0:
        small.append(i)
        if i != n // i:
            big.append(n // i)
    i += 1

numlist = small + big[::-1]

for i in range(len(numlist)):
    print(numlist[i])