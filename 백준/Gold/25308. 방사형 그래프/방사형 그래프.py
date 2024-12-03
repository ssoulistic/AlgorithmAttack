import sys
input=sys.stdin.readline
import math
ab=list(map(int,input().split()))
coord=[]
for i in range(8):
    coord.append([math.sin(math.pi*(45*i/180)),math.cos(math.pi*(45*i)/180)])

def ccw(p1,p2,p3):
    ccw=(p2[0]-p1[0])*(p3[1]-p1[1])-(p2[1]-p1[1])*(p3[0]-p1[0])
    return int(ccw/abs(ccw)) if ccw!=0 else 0

count=0
def dfs(bucket,added):
    global count
    if len(bucket)>=3:
        if ccw(bucket[-3],bucket[-2],bucket[-1])>0:
            return
    if len(bucket)==8:
        if ccw(bucket[-2],bucket[-1],bucket[0])<=0 and ccw(bucket[-1],bucket[0],bucket[1])<=0:
            count+=1
        return
    for i in range(8):
        if not added[i]:
            x,y=coord[len(bucket)]
            bucket.append([ab[i]*x,ab[i]*y])
            added[i]=True
            dfs(bucket,added)
            added[i]=False
            bucket.pop()
    return
added=[False for _ in range(8)]
dfs([],added)
print(count)