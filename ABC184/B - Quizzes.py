nx = [int(x) for x in input().split()]
s = input()

for i in range(nx[0]):
    if s[i] == 'o':
        nx[1] += 1
    elif nx[1] != 0:
        nx[1] -= 1

print(nx[1])