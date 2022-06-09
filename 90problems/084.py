n = int(input())
s = input()
length, no = 1, 0
for i in range(1, n):
    if s[i-1] == s[i]:
        length += 1
        if i == n-1:
            no += length*(length-1)//2
    else:
        no += length*(length-1)//2
        length = 1
print(n*(n-1)//2-no)