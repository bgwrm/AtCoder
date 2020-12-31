n = int(input())
p = 2025 - n
ans = []

for i in range(1,10):
    if p%i == 0 and p//i < 10:
        ans += [[i, p//i]]

for i in ans:
    print(str(i[0]) + ' x ' + str(i[1]))