n = int(input())
l = [int(_) for _ in input().split()]
ans = 0

for i in range(0, len(l)-2):
    for j in range(i+1, len(l)-1):
        for k in range(j+1, len(l)):
            if l[i] != l[j] and l[j] != l[k] and l[k] != l[i] and l[i] + l[j] > l[k] and l[j] + l[k] > l[i] and l[k] + l[i] > l[j]:
            	ans += 1

print(ans)