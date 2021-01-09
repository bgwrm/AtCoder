ns = (input().split())
n, s = int(ns[0]), ns[1]
ans = 0
for i in range(n):
    dic = {'A':0,'T':0,'G':0,'C':0}
    for j in range(i,n):
        dic[s[j]] += 1
        if dic['A'] == dic['T'] and dic['C'] == dic['G']:
            ans += 1
print(ans)