from collections import deque
import sys
N,M=map(int,sys.stdin.readline().strip().split())
graph=[[] for _ in range(N+1)]
for _ in range(M):
    A,B=map(int,sys.stdin.readline().strip().split())
    if B not in graph[A]:
        graph[A].append(B)
        graph[B].append(A)

que=deque()
def kev(start,target):
    visited=[0 for _ in range(N+1)]
    if not visited[start]:
        visited[start]=1
        que.append(start)
        while que:
            next=que.popleft()
            for node in graph[next]:
                if not visited[node]:
                    visited[node]=visited[next]+1
                    que.append(node)
    return visited[target]-1

answer=[0]*N
mini=(100*100+1,0)
for i in range(1,N+1):
    for j in range(1,N+1):
        if i!=j:
            answer[i-1]+=(kev(i,j))
    if mini[0]>answer[i-1]:
        mini=(answer[i-1],i)
print(mini[1])