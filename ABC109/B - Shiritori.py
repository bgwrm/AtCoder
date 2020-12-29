n = int(input())
l = [input() for _ in range(n)]

if len(l) != len(set(l)):
    print('No')
    exit()

for i in range(n-1):
    if l[i][-1] != l[i+1][0]:
        print('No')
        exit()
print('Yes')