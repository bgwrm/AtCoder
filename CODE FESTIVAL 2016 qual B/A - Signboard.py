s = input()
c = 'CODEFESTIVAL2016'
print(sum(s[i] != c[i] for i in range(len(s))))