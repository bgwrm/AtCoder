n = int(input())
for h in range(1, 3501):
    for w in range(1, 3501):
        if (4*h*w-n*h-n*w) != 0 and (n*h*w)/(4*h*w-n*h-n*w) > 0 and (n*h*w)%(4*h*w-n*h-n*w) == 0:
            print(h, w, (n*h*w)//(4*h*w-n*h-n*w))
            exit()