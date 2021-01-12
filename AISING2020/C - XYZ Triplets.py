n = int(input())
l = [0]*(10**4+1)
for x in range(1,100):
    for y in range(1,100):
        for z in range(1,100):
            num = x*x+y*y+z*z+x*y+y*z+z*x
            if num <= 10000:
                l[num] += 1
for i in range(n):
    print(l[i+1])