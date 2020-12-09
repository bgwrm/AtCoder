import sys

NY = [int(i) for i in input().split()]

for i in range(NY[0] + 1):
    for j in range(NY[0] - i + 1):
            if 10000 * i + 5000 * j + 1000 * (NY[0] - i - j) == NY[1]:
                print(str(i) + ' ' + str(j) + ' ' + str(NY[0] - i - j))
                sys.exit()

print('-1 -1 -1')