import sys
T=int(sys.stdin.readline())
conf=[]
for _ in range(T):
    conf.append(list(map(int,sys.stdin.readline().split())))
conf.sort()
last=0
count=0
for c1 in conf:
    if c1[0]>=last:
        last=c1[1]
        count+=1
    elif c1[1]<=last:
        last=c1[1]
print(count)

