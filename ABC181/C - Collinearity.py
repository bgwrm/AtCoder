import itertools

n = int(input())
xy = [[int(_) for _ in input().split()] for n in range(n)]
combi = list(itertools.combinations(xy, 3))

for i in range(len(combi)):
    if (combi[i][1][0] - combi[i][0][0])*(combi[i][2][1] - combi[i][0][1]) == (combi[i][2][0] - combi[i][0][0])*(combi[i][1][1] - combi[i][0][1]):
        print('Yes')
        exit()

print('No')