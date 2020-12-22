n = int(input())
s = [int(input()) for i in range(n)]

if sum(s)%10 != 0:
    print(sum(s))
    exit()

num = 100
for i in s:
    if i%10 != 0:
        num = min(num, i)

if (sum(s) - num)%10 != 0:
    print(sum(s) - num)
else:
    print(0)