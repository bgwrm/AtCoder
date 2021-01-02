n = int(input())
s = [input()[::-1] for _ in range(n)]
set_s = sorted(list(set(s)))

for i in range(len(set_s)-1):
    if set_s[i+1] == set_s[i]+'!':
        print(set_s[i][::-1])
        exit()
print('satisfiable')