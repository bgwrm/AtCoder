n = int(input())
s = input()
li, co, mod = list('atcoder'), [0]*7, 10**9+7
for i in s:
    if i not in li: continue
    index = li.index(i)
    if index == 0: co[0] += 1
    else: co[index] = (co[index]+co[index-1])%mod
print(co[-1]%mod)