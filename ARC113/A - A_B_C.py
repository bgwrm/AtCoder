k = int(input())
ans = 0
for i in range(1, k+1):
    for j in range(i, k+1):
        if i*j <= k:
            for l in range(j, k+1):
                if i*j*l <= k:
                    p = len(set([i,j,l]))
                    if p == 3:
                        ans += 6
                    elif p == 2:
                        ans += 3
                    else:
                        ans += 1
                else:
                    break
        else:
            break
print(ans)