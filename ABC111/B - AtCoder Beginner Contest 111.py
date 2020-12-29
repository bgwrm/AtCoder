n = int(input())

while True:
    if str(n) == str(n)[0]*len(str(n)):
        print(n)
        exit()
    n += 1