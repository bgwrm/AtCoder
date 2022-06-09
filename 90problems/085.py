k, ans = int(input()), 0
for i in range(1, k+1):
    if i**3 > k: break
    if k%i > 0: continue
    ato = k//i
    for j in range(i, k+1):
        if j**2 > ato: break
        if ato%j == 0: ans += 1
print(ans)