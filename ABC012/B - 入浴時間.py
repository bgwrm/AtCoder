n = int(input())
print(str(n//3600).zfill(2)+':'+str(n//60%60).zfill(2)+':'+str(n%60).zfill(2))