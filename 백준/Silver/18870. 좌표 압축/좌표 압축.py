import sys
n=int(sys.stdin.readline())
coord=list(map(int,sys.stdin.readline().split()))
dic=dict()
for idx,c in enumerate(sorted(set(coord))):
    dic[c]=idx
for i in coord:
    print(dic[i],end=' ')