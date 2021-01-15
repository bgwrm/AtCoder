a = int(input())
for i in range(10,10001):
    n = 0
    for j in range(len(str(i))):
        n += int(str(i)[-j-1])*i**j
    if a == n:
        print(i)
        exit()
print(-1)