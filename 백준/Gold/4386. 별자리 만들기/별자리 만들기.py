import sys
input=sys.stdin.readline
from heapq import *
n=int(input())
star=[]
visit=[False for _ in range(n)]
def distance(a,b):
    x1,y1=a
    x2,y2=b
    return ((x2-x1)**2+(y2-y1)**2)**0.5

for _ in range(n):
    x,y=map(float,input().split())
    star.append([x,y])

visit[0]=True
queue=[]
for i in range(1,n):
    queue.append([distance(star[0],star[i]),[0,i]])

answer=0
heapify(queue)
while queue:
    cost,[start,end]=heappop(queue)
    if not visit[end]:
        visit[end]=True
        answer+=cost
        for k in range(n):
            if not visit[k]:
                heappush(queue,[distance(star[end],star[k]),[end,k]])
print(round(answer,2))