n = int(input())
a = [int(_) for _ in input().split()]
q = int(input())
bc = [[int(_) for _ in input().split()] for n in range(q)]
numlist = [0] * (10**5 + 1)
sum = 0

for i in a:
    numlist[i] += 1
    sum += i

for i in range(q):
    sum += numlist[bc[i][0]]*(bc[i][1]-bc[i][0])
    numlist[bc[i][1]] += numlist[bc[i][0]]
    numlist[bc[i][0]] = 0
    print(sum)