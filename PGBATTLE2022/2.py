n = int(input())
a = [(int(_), i) for i, _ in enumerate(input().split(), 1)]
sorted_a = sorted(a)
ans_list = []
for i in range(n, 2*n):
    ans_list += [sorted_a[i][1]]
print(*sorted(ans_list), sep='\n')