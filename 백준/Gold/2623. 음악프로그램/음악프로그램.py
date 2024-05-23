import sys
input=sys.stdin.readline
from collections import deque
N,M=map(int,input().split())
graph=[[] for _ in range(N)]
indegree=[0]*N
for _ in range(M):
    num,*seq=map(int,input().split())
    for i in range(num-1):
        graph[seq[i]-1].append(seq[i+1]-1)
        indegree[seq[i+1]-1]+=1
queue=deque()
for j in range(N):
    if indegree[j]==0:
        queue.append(j)
answer=[]
while queue:
    v=queue.popleft()
    answer.append(v+1)
    for next in graph[v]:
        indegree[next]-=1
        if indegree[next]==0:
            queue.append(next)
if len(answer)!=N:
    print(0)
else:
    print(*answer,sep="\n")
        