des, dis = (int(_) for _ in input().split())
dir_list = ['NNE','NE','ENE','E','ESE','SE','SSE','S','SSW','SW','WSW','W','WNW','NW','NNW','N']
dis_list = [2,15,33,54,79,107,138,171,207,244,284,326]
w = 0

d = dir_list[(des-113)//225]

for i in dis_list:
    if dis <= i*6+2:
        break
    w += 1

print('C' if w == 0 else d, w)