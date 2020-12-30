x = int(input())
ans = 1

for i in range(1, int(x**0.5)+1):
    for j in range(2, x+1):
        if i**j <= x:
            ans = max(ans, i**j)
        else:
            continue

print(ans)