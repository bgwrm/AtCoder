import math
w = int(input())
s = 'DiscoPresentsDiscoveryChannelProgrammingContest2016'
for i in range(math.ceil(len(s)/w)):
    print(s[w*i:w*(i+1)])