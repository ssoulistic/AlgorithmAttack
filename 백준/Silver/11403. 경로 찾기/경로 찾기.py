import sys
T=int(sys.stdin.readline())
graph=[[] for _ in range(T)]
for i in range(T):
    line=list(map(int,sys.stdin.readline().split()))
    for j in range(T):
        if line[j]==1:
            graph[i].append(j)
        
que=[]
for l in range(T):
    visited=[0]*T
    for k in graph[l]:
        que.append(k)
        while que:
            next=que.pop()
            visited[next]=1
            for g in graph[next]:
                if not visited[g]:
                    visited[g]=1
                    que.append(g)
    print(*visited)