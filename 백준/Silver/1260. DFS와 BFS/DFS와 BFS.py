N,M,V=map(int,input().split())
gp=[[] for _ in range(N+1)]

for _ in range(M):
    a1,a2=map(int,input().split())
    gp[a1].append(a2)
    gp[a2].append(a1)

def dfs(graph,start,visited=[]):
    visited.append(start)
    for node in sorted(graph[start]):
        if node not in visited:
            dfs(graph,node,visited)
    return visited

def bfs(graph,start):
    visit=[]
    queue=[]
    queue.append(start)

    while queue:
        node = queue.pop(0)
        if node not in visit:
            visit.append(node)
            queue.extend(sorted(graph[node]))
    return visit

print(*dfs(gp,V))
print(*bfs(gp,V))