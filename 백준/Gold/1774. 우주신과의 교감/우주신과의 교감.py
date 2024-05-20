import sys
input=sys.stdin.readline
from heapq import *
from collections import deque
N,M=map(int,input().split())

def distance(p,q):
    x1,y1=p
    x2,y2=q
    return ((x1-x2)**2+(y1-y2)**2)**0.5

gods=[]
for _ in range(N):
    X,Y=map(int,input().split())
    gods.append([X,Y])
graph=[[] for _ in range(N)]

for _ in range(M):
    a,b=map(int,input().split())
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)

# 1. 0에 연결된 좌표들 모두 탐색하며 가능한 나머지 간선들 관계를 모두 heap에 넣기.
# 2. heap에서 빼면서 채택하기 => 채택된 좌표와 연결된 간선들과의 관계 모두 heap, 이전의 결과들은 connected라면 제외 아니면
connected=[False]*N
connected[0]=True

queue=deque()
queue.append(0)
while queue:
    next=queue.popleft()
    connected[next]=True
    for n2 in graph[next]:
        if not connected[n2]:
            queue.append(n2)

star_heap=[]
for i in range(N):
    if connected[i]:
        for j in range(N):
            if not connected[j]:
                heappush(star_heap,[distance(gods[i],gods[j]),i,j])

answer=0
while star_heap:
    val,z1,z2=heappop(star_heap)
    if not connected[z2]:
        answer+=val
        queue2=deque()
        queue2.append(z2)
        queue3=[]
        while queue2:
            next2=queue2.popleft()
            connected[next2]=True
            queue3.append(next2)
            for next_z2 in graph[next2]:
                if not connected[next_z2]:
                    queue2.append(next_z2)
        for i in queue3:
            for j in range(N):
                if not connected[j]:
                    heappush(star_heap,[distance(gods[i],gods[j]),i,j])
print(f"{round(answer,2):.2f}")
