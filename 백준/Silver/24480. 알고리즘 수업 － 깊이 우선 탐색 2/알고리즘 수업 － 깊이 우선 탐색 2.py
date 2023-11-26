import sys
sys.setrecursionlimit(10**9)
N,M,R=map(int,sys.stdin.readline().split())
graph=[[] for _ in range(N+1)]
visited=[0 for _ in range(N+1)]
count=1

def dfs(G,start):
    global count
    visited[start]=count
    for x in sorted(G[start],reverse=True):
        if not visited[x]:
            count+=1
            dfs(G,x)

for _ in range(M):
    u,v=map(int,sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)
dfs(graph,R)

for l in visited[1:]:
    print(l)