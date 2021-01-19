n = int(input())
b = [int(_) for _ in input().split()]
ans = []
for i in b:
    if i-1 > len(ans):
        print(-1)
        exit()
    ans.insert(i-1, i)
print(*ans, sep='\n')