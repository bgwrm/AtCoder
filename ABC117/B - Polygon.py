n = int(input())
l = [int(_) for _ in input().split()]

for i in l:
    if sum(l) - i <= i:
        print('No')
        exit()
print('Yes')