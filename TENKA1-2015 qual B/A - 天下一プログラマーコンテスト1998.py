l = [1, 1, 2]
for i in range(17):
    l += [l[-1]+l[-2]+l[-3]]
print(l[-1]*100)